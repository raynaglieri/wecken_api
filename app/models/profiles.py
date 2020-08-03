from typing import Optional

from mongoengine import EmbeddedDocument
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import FileField

from pydantic import BaseModel

from app.core.settings import user as user_settings


class Profile(EmbeddedDocument):
    """
    Mongo Engine Profile Model.
    """
    bio = StringField(max_length=user_settings['profile']['max_length'])
    # photos = ListField(FileField())

    meta = {
        'collection': 'users'
    }

class ProfileModel(BaseModel):
    """
    API Profile Model.
    """
    bio: Optional[str] = None
    # photos = Optional[]