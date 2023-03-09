import uuid

from mongoengine import (
    Document,
    StringField,
    DateField,
    EnumField,
    UUIDField
)
from app.core.constants import TurnInterval


class Turn(Document):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, binary=False)
    name = StringField(required=True, max_length=100)
    document = StringField(required=True, max_length=10)
    date = DateField(required=True)
    hour = EnumField(TurnInterval, required=True)

    def to_json(self):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "document": self.document,
            "date": str(self.date),
            "hour": self.hour,
        }
