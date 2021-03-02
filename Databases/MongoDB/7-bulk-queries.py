from pymongo import MongoClient
import datetime
import pprint

client = MongoClient()                          ## Connecting to client

db = client.test_database                       ## Connect to db

posts = db.posts                                ## Collection

### *** find() *** ###

for post in posts.find():
    pprint.pprint(post)
    print("---------------------------------")

## We can even query for specific documents
print("+++++++++++++++++++++++++++++++++++++++++++")
print("Documents authored by 'Mike':")
for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)
    print("----------------------------------")