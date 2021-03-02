#Finding the documents from the collection
import pymongo

from pymongo import MongoClient
client=MongoClient()
dbs=client.database_names()
db=client.pyex #db pyex
docs=db.pycoll.find({})
for doc in docs:
    print (doc)

