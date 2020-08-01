# Services to perform on user objects.

from typing import List, Optional
from bcrypt import hashpw, gensalt
from app.models.users import User


def password_hash(password: str):
    byte_pass = str.encode(password)
    return hashpw(byte_pass, gensalt())


def create(name: str, email: str, password: bytes) -> User:
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
