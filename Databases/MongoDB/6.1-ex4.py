#inserting more docs
import datetime
import pymongo
from pymongo import MongoClient
client=MongoClient()
#dbs=client.database_names()
db=client.pyex #db pyex
coll=db.pycoll

new_posts = [{"author": "Mike",
"text": "Another post!",
"tags": ["bulk", "insert"],
"date": datetime.datetime(2009, 11, 12, 11, 14)
},
{"author": "Eliot",
"title": "MongoDB is fun",
"text": "and pretty easy too!",
"date": datetime.datetime(2009, 11, 10, 10, 34)
}]

coll.insert(new_posts)
print (coll.count())
s=coll.find({})
for ss in s:
    print (ss)

