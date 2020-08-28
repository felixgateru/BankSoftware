from data.accounts import Account
from data.mongo_setup import mongo_setup

from datetime import datetime
mongo_setup()


account_number = input('Please enter an account number:')
creation_date = datetime.now()
balance = float(input('Please enter your account balance:'))
last_date = datetime.now()

x = Account()
x.account_number = account_number
x.creation_date = creation_date
x.balance = balance
x.last_date = last_date
x.save()
print("account successfully created")