import mongoengine
from data.transactions import Transaction


class Account(mongoengine.Document):

    account_number = mongoengine.StringField(required=True)
    creation_date = mongoengine.DateTimeField(required=True)
    balance = mongoengine.DecimalField()
    transactions = mongoengine.EmbeddedDocumentListField(Transaction)
    last_date = mongoengine.DateTimeField(required=True)

    meta = {
        'db_alias': 'core',
        'collections': 'accounts'
    }
