from pymongo import MongoClient
import datetime

client = MongoClient()                          ## Connecting to client

db = client.test_database                       ## Connect to db

posts = db.posts                                ## Collection

print("Total documents in 'posts' collection: ", posts.count())

print("++++++++++++++++++++++++++++++++++++")

## count of those documents that match a specific query

print("Count of the documents authored by Mike: ", posts.find({"author": "Mike"}).count())