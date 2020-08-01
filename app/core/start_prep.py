# Functions called before API is live.

import os

from mongoengine import connect

from app.core.settings import system_information
from app.core.settings import database


def propogate_settings():
    """
    Set environment variables as settings if they exists.
    """
    if "ENVIRONMENT" in os.environ:
        system_information["ENVIRONMENT"] = os.environ["ENVIRONMENT"]

    if "CIRCLE_SHA1" in os.environ:
        system_information["BUILD"] = os.environ["CIRCLE_SHA1"]

    if "DB_CONNECTION_STRING" in os.environ:
        database["CONNECTION_STRING"] = os.environ["CIRCLE_SHA1"]


def mongo_init():
    """
    Initialize connection to MongoDB.
    """
    connection_string = database["CONNECTION_STRING"]
    if connection_string:
        connect(host=database["CONNECTION_STRING"])
    elif system_information["ENVIRONMENT"].lower() == "development":
        connect(database["LOCAL_DB_NAME"])
