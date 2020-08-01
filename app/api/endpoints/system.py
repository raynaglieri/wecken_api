from typing import Any

from fastapi import APIRouter

from app.core.settings import system_information

router = APIRouter()


@router.get("/")
def get_system_information() -> Any:
    """
    Provides information about the current application.
    """
    return system_information
