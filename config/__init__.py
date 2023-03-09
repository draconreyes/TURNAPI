import os
from mongoengine import connect
from fastapi import FastAPI
from app.api.routers import router

connect(host=os.getenv("MONGOURI"))

app = FastAPI(
        title="TURN API",
        version="v1",
        docs_url="/docs"
    )

app.include_router(
    router
)
