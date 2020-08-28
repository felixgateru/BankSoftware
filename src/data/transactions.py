import mongoengine
from datetime import datetime


class Transaction(mongoengine.EmbeddedDocument):
    id = mongoengine.ObjectIdField()
    date = mongoengine.DateTimeField(default=datetime.now, required=True)
    value = mongoengine.DecimalField(required=True)
    type = mongoengine.StringField(required=True)
