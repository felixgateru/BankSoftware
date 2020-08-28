from data.accounts import Account

from data.mongo_setup import mongo_setup

mongo_setup()

x =list(Account.objects())
for i in x:
    print(i.id)