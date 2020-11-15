# mongo-engine packages
from mongoengine import Document, StringField, FloatField, URLField, IntField, DateTimeField, ReferenceField, ListField

# First go with non-relational, not sure if I'm doing this right, but it 'feels' right...

class Sport(Document):
    sport_id = StringField()
    name = StringField()

class Selections(Document):
    selection_id = StringField()
    name = StringField()
    odds = FloatField()

class Market(Document):
    market_id = StringField()
    name = StringField()
    selections = ListField(ReferenceField(Selection))

class Events(Document):

    id = StringField()
    url = URLField()
    name = StringField(required=True)
    startTime = DateTimeField()
    sport = ReferenceField(Sport)
    markets = ReferenceField(Market)
