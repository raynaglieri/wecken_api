# Main entry point for wecken API.

from fastapi import FastAPI

from app.api.api import api_router
from app.core.start_prep import propogate_settings
from app.core.start_prep import mongo_init

propogate_settings()
mongo_init()
app = FastAPI()
app.include_router(api_router)
