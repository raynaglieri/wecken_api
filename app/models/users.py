from typing import Optional

from mongoengine import Document
from mongoengine import StringField
from mongoengine import ReferenceField
from mongoengine import EmbeddedDocumentField

from pydantic import BaseModel

from app.models.profiles import Profile
from app.models.profiles import ProfileModel


class User(Document):
    """
    Mongo Engine User Model.
    """
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    profile = EmbeddedDocumentField(Profile)

    meta = {
        'collection': 'users'
    }

class UserModel(BaseModel):
    """
    API User Model.
    """
    name: str 
    password: str 
    email: str
    profile: Optional[ProfileModel] = None

