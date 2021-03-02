from pymongo import MongoClient

client = MongoClient()

## Getting a collection in PyMongo works the same as getting a database

db = client.test_database

collection = db.test_collection

## or (using dictionary style access)

#collection = db['test-collection']

print(collection)