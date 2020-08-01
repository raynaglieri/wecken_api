from mongoengine import Document
from mongoengine import StringField
from mongoengine import BinaryField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import EmbeddedDocumentField

from app.models.matches import Match
from app.models.profiles import Profile


class User(Document):
    """
    Mongo Engine User Model.
    """
    name = StringField(required=True)
    email = StringField(required=True)
    password = BinaryField(required=True)
    profile = EmbeddedDocumentField(Profile)
    matches = ListField(ReferenceField(Match))

    meta = {
        'collection': 'users'
    }
