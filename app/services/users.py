# Services to perform on user objects.

from typing import List, Optional
from app.models.users import User


def create(name: str, email: str, password: str) -> User:
    """
    Create user object from model and save to db.
    """
    user = User()
    user.name = name
    user.email = email
    user.password = password
    user.save()
    return user


def find_by_email(email: str) -> User:
    """
    Find user by email in db.
    """
    return User.objects(email=email).first()
