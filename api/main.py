# import json
# import os
# import time
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request

# from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

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

    @app.get("/api/search")
    def search(request: Request):
        ##
        return

    return app


app = create_app(app=FastAPI())

if __name__ == "__main__":
    import uvicorn

    app = create_app(app=FastAPI())
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
