import mongoengine
from datetime import datetime


class Customer(mongoengine.Document):
    reg_date = mongoengine.DateTimeField(default=datetime.now)
    id = mongoengine.ObjectIdField()

    first_name = mongoengine.StringField(required=True)
    sur_name = mongoengine.StringField(required=True)
    middle_name = mongoengine.StringField(required=False, default=" ")
    age = mongoengine.IntField(required=True, min_value=0, max_value=120)
    gender = mongoengine.StringField(required=True)
    DOB = mongoengine.DateTimeField(required=True)
    Nat_Id_No = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collections': 'customers'
    }
