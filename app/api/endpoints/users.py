# Enpoint for user object operations.

from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from app.services.users import create
from app.services.users import find_by_email
from app.services.users import password_hash


router = APIRouter()


@router.post("/")
def create_user() -> Any:
    """
    Create new user.
    If the user exists, an exception is raised.
    """
    sample_name = "sample"
    sample_email = "sample@sample.com"
    sample_pass = "sample_pass"

    if find_by_email(sample_email):
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = create(sample_name, sample_email, password_hash(sample_pass))
    return user
