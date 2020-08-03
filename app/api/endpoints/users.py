# Enpoint for user object operations.

from typing import Any, List

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.models.users import UserModel
from app.services.users import create
from app.services.users import find_by_email


router = APIRouter()


@router.post("/")
def create_user(user: UserModel) -> Any:
    """
    Create new user.
    If the user exists, an exception is raised.
    """

    if find_by_email(user.email):
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = create(user.name, user.email, user.password)
    return user
