import json
import os
from datetime import datetime

# import nest_asyncio
import requests
from dotenv import load_dotenv
from llama_index.core import (
    DocumentSummaryIndex,
    SimpleDirectoryReader,
    get_response_synthesizer,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_parse import LlamaParse

load_dotenv()
# nest_asyncio.apply()

pacer_username = os.getenv("PACER_USERNAME")
pacer_password = os.getenv("PACER_PASSWORD")
auth_token = os.getenv("COURT_LISTENER_API_KEY")
llama_cloud_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

FILES_METADATA = dict()


def search_court_listener(query, type=None, start_page=1, max_pages=None):
    search_url = "https://www.courtlistener.com/api/rest/v3/search/"
    all_results = []
    current_page = start_page
    while True:
        params = {
            "q": query,
            "type": type if type else None,
            "page": current_page,
        }
        headers = {"Authorization": f"Token {auth_token}"}

        response = requests.get(search_url, params=params, headers=headers)

        if response.ok:
            print(f"Search successful for page {current_page}.")
            data = response.json()
            all_results.extend(data.get("results", []))

            # Check if there is a next page and if max_pages limit is not reached
            next_page = data.get("next")
            if next_page and (
                max_pages is None or current_page < start_page + max_pages - 1
            ):
                current_page += 1
            else:
                break
        else:
            print(f"Search failed for page {current_page}.")
            print(response.text)
            break

    if all_results:
        # Create a directory for storing data if it doesn't exist
        os.makedirs("data_json", exist_ok=True)
        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"data_json/{timestamp}_{query}.json"
        # Save the JSON data to the file
        with open(filename, "w") as f:
            json.dump(all_results, f, indent=4)
        print(f"Data saved to {filename}")
        print(json.dumps(all_results, indent=4))

    return all_results if all_results else None


def get_case_info(
    request_type=1,
    docket_number="5:16-cv-00432",
    court="okwd",
    recap_document=None,
):
    payload = {
        "request_type": request_type if request_type else None,
        "recap_document": recap_document if recap_document else None,
        "docket_number": docket_number if docket_number else None,
        "court": court if court else None,
        "pacer_username": pacer_username,
        "pacer_password": pacer_password,
    }

    headers = {"Authorization": f"Token {auth_token}"}

    response = requests.post(
        "https://www.courtlistener.com/api/rest/v3/recap-fetch/",
        data=payload,
        headers=headers,
    )

    if response.ok:
        print("Request successful.")
        print(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print("Request failed.")
        print(response.text)


def get_download_url(filepath_local):
    print(filepath_local)
    filepath_local = filepath_local.replace("/storage", "")

    return f"https://storage.courtlistener.com{filepath_local}"


def download_file_from_url(url, path):
    response = requests.get(url)

    if response.ok:
        filepath = os.path.join(path, url.split("/")[-1])
        print(filepath)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"File saved to {path}")


def get_file_metadata(filename):
    fname = filename.split("/")[-1]
    return FILES_METADATA[fname]


def build_index():
    # Use LlamaParse to extract text from PDFs.
    parser = LlamaParse(
        api_key=llama_cloud_api_key,
        result_type="text",
        verbose=True,
    )
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(
        "./data",
        file_extractor=file_extractor,
        file_metadata=get_file_metadata,
    ).load_data()

    chatgpt = OpenAI(temperature=0, model="gpt-3.5-turbo")
    splitter = SentenceSplitter(chunk_size=1024)
    response_synthesizer = get_response_synthesizer(
        response_mode="tree_summarize", use_async=True
    )
    doc_summary_index = DocumentSummaryIndex.from_documents(
        documents,
        llm=chatgpt,
        transformations=[splitter],
        response_synthesizer=response_synthesizer,
        show_progress=True,
    )
    doc_summary_index.storage_context.persist(persist_dir="./citation")


if __name__ == "__main__":
    query = "bitcoin"
    max_pages = 2
    results = search_court_listener(query, type="r", max_pages=max_pages)

    results = {"results": results, "count": len(results)}
    count = results["count"]
    list_results = results["results"]
    list_result_filtered = []
    print(len(list_results))
    for list_result in list_results:
        if list_result["is_available"] is False:
            continue
        legal_info = {
            "case_name": list_result["caseName"],
            "docket_number": list_result["docketNumber"],
            "court": list_result["court"],
            "date_filed": list_result["dateFiled"],
            "date_terminated": list_result["dateTerminated"],
            "assigned_to": list_result["assignedTo"],
            "cause": list_result["cause"],
            "jurisdiction_type": list_result["jurisdictionType"],
            "suit_nature": list_result["suitNature"],
            "document_number": list_result["document_number"],
            "page_count": list_result["page_count"],
            "is_available": list_result["is_available"],
            "filepath_local": list_result["filepath_local"],
            "download_url": get_download_url(list_result["filepath_local"]),
            "description": list_result["description"],
        }
        list_result_filtered.append(legal_info)
        fname = list_result["filepath_local"].split("/")[-1]
        FILES_METADATA[fname] = legal_info

    url_list = [x["download_url"] for x in list_result_filtered]

    # # Save the filtered results to a JSON file in the data directory
    # with open("data/list_result_filtered.json", "w") as json_file:
    #     json.dump(list_result_filtered, json_file, indent=4)
    # print("Filtered results saved to data/list_result_filtered.json")

    print(url_list)
    for url in url_list:
        try:
            url = url.replace("comrecap", "com/recap")
            download_file_from_url(url, "data")
        except Exception as e:
            print(e)

    build_index()
