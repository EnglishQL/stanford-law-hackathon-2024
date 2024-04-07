# import json
# import os
# import time
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request

# from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from fastapi.responses import JSONResponse

origins = ["http://localhost:3000"]


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
        results = [
            {
                "case_name": "Crosthwaite v. R E Serrano, Inc",
                "docket_number": "3:07-cv-01697",
                "court": "District Court, N.D. California",
                "date_filed": "2007-03-23T00:53:00-07:00",
                "date_terminated": "2007-12-05T23:53:00-08:00",
                "assigned_to": "Maxine M. Chesney",
                "cause": "29:1132 E.R.I.S.A.: Employee Benefits",
                "jurisdiction_type": "Federal question",
                "suit_nature": "Labor: E.R.I.S.A.",
                "document_number": 9,
                "page_count": 2,
                "id": 1,
                "is_available": True,
                "filepath_local": "/storage/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.9.0.pdf",
                "download_url": "https://storage.courtlistener.com/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.9.0.pdf",
                "description": "ORDER approving substitution of attorney for plaintiffs.  Signed by Judge Maxine M. Chesney on 6/7/2007. (mmclc2, COURT STAFF) (Filed on 6/7/2007)",
                "download_url": "https://storage.courtlistener.com/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.9.0.pdf",
                "text": "Nisl letius convallis id risus mattis laoreet hac leo rhoncus pede suspendisse orci penatibus maximus potenti pharetra mollis curabitur integer luctus odio euismod sodales class conubia tellus quisque porttitor mus sapien nostra lacus blandit pellentesque fames vulputate litora molestie ligula sit cubilia congue aliquet tortor cras lobortis netus aptent sed velit dolor enim quis massa ipsum sagittis feugiat ornare at diam vivamus porta dictum urna turpis amet volutpat faucibus posuere praesent hendrerit vestibulum iaculis montes taciti lectus eros et",
            },
            {
                "case_name": "Crosthwaite v. R E Serrano, Inc",
                "docket_number": "3:07-cv-01697",
                "court": "District Court, N.D. California",
                "date_filed": "2007-03-23T00:53:00-07:00",
                "date_terminated": "2007-12-05T23:53:00-08:00",
                "assigned_to": "Maxine M. Chesney",
                "cause": "29:1132 E.R.I.S.A.: Employee Benefits",
                "jurisdiction_type": "Federal question",
                "suit_nature": "Labor: E.R.I.S.A.",
                "document_number": 14,
                "page_count": 2,
                "id": 2,
                "is_available": True,
                "filepath_local": "/storage/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.14.0.pdf",
                "download_url": "https://storage.courtlistener.com/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.14.0.pdf",
                "description": "ORDER by Judge Maxine M. Chesney granting  13  Motion to Continue Case Management Conference to September 7, 2007 at 10:30 a.m.  (mmclc2, COURT STAFF) (Filed on 6/20/2007)",
                "download_url": "https://storage.courtlistener.com/recap/gov.uscourts.cand.190473/gov.uscourts.cand.190473.9.0.pdf",
                "text": "Nisl letius convallis id risus mattis laoreet hac leo rhoncus pede suspendisse orci penatibus maximus potenti pharetra mollis curabitur integer luctus odio euismod sodales class conubia tellus quisque porttitor mus sapien nostra lacus blandit pellentesque fames vulputate litora molestie ligula sit cubilia congue aliquet tortor cras lobortis netus aptent sed velit dolor enim quis massa ipsum sagittis feugiat ornare at diam vivamus porta dictum urna turpis amet volutpat faucibus posuere praesent hendrerit vestibulum iaculis montes taciti lectus eros et",
            },
        ]
        # return jsonable_encoder(results)

        return JSONResponse(content=results)

    return app


app = create_app(app=FastAPI())

if __name__ == "__main__":
    import uvicorn

    app = create_app(app=FastAPI())
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
