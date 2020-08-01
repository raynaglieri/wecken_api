from mongoengine import Document
from mongoengine import StringField


class Match(Document):
    """
    Mongo Engine Match Model.
    """
    location = StringField()

    meta = {
        'collection': 'matches'
    }
