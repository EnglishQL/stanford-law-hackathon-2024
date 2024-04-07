import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


pacer_username = os.getenv("PACER_USERNAME")
pacer_password = os.getenv("PACER_PASSWORD")
auth_token = os.getenv("COURT_LISTENER_API_KEY")


def get_case_info(request_type=1, docket_number="5:16-cv-00432", court="okwd"):
    payload = {
        "request_type": request_type,
        "docket_number": docket_number,
        "court": court,
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


def get_pdf(request_type=2, recap_document=112):
    pdf_response = requests.post(
        "https://www.courtlistener.com/api/rest/v3/recap-fetch/",
        data={
            "request_type": request_type,
            "recap_document": recap_document,
            "pacer_username": pacer_username,
            "pacer_password": pacer_password,
        },
        headers={"Authorization": f"Token {auth_token}"},
    )

    if pdf_response.ok:
        print("PDF request successful.")
        return pdf_response.content
    else:
        print("PDF request failed.")
        print(pdf_response.text)


if __name__ == "__main__":
    get_case_info(
        request_type=1, docket_number="riches-v-roe-v-wade-410-us-113", court="txnd"
    )
    # get_pdf()
