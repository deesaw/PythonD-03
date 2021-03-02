from pymongo import MongoClient
import pprint

client = MongoClient()                          ## Connecting to client

db = client.test_database                       ## Connect to db

posts = db.posts                                ## Access collection 'posts'

### *** most basic type of query that can be performed in MongoDB is find_one() *** ###
"""returns a single document matching a query (or None if there are no matches)"""

print("The first document:")
pprint.pprint(posts.find_one())
print('---------------------------------')

print("The first post with author Mike:")
pprint.pprint(posts.find_one({"author": "Mike"}))
print('---------------------------------')

## try with a different author, like “Eliot”, we’ll get no result:
print("The first post with author Elliot:")
print(posts.find_one({"author": "Eliot"}))
