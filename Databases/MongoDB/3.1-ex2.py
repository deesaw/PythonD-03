#inserting a document in to collection
import pymongo

from pymongo import MongoClient
client=MongoClient()
dbs=client.database_names()
db=client.pyex #db pyex
db.pycoll.insert_one({"Name":"Ram","Age":10,"Gender":"M"}) #inserting a doc in to collection pycoll 
print("Successfully inserted record")
