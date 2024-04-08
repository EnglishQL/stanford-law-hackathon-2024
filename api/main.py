# import json
# import os
# import time
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()
# from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from llama_index.core import StorageContext, load_index_from_storage

# from fastapi.responses import JSONResponse

origins = ["http://localhost:3000"]

index = load_index_from_storage(
    StorageContext.from_defaults(persist_dir="./citation")
)

retriever = index.as_retriever()


def create_app(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    load_dotenv()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.post("/api/search")
    async def search(request: Request):
        body = await request.json()
        query = body.get("query", "")
        print(query)
        nodes = retriever.retrieve(query)
        # print(nodes)
        results = []
        for node in nodes:
            result = {
                "text": node.text,
                "case_name": node.metadata["case_name"],
                "docket_number": node.metadata["docket_number"],
                "court": node.metadata["court"],
                "date_filed": node.metadata["date_filed"],
                "date_terminated": node.metadata["date_terminated"],
                "assigned_to": node.metadata["assigned_to"],
                "cause": node.metadata["cause"],
                "jurisdiction_type": node.metadata["jurisdiction_type"],
                "suit_nature": node.metadata["suit_nature"],
                "document_number": node.metadata["document_number"],
                "page_count": node.metadata["page_count"],
                "is_available": node.metadata["is_available"],
                "filepath_local": node.metadata["filepath_local"],
                "download_url": node.metadata["download_url"],
                "description": node.metadata["description"],
            }
            print(result)
            results.append(result)

        return JSONResponse(content=results)

    return app


app = create_app(app=FastAPI())

if __name__ == "__main__":
    import uvicorn

    app = create_app(app=FastAPI())
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
