from pymongo import MongoClient
import datetime

client = MongoClient()                          ## Connecting to client

db = client.test_database                       ## Connect to db


## In PyMongo we use dictionaries to represent documents

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()     ## Python types will be automatically converted to the appropriate BSON types.
    }

### *** Inserting a Doucument *** ###
posts = db.posts                  ## Creating collection 'posts'

post_id = posts.insert_one(post).inserted_id    # inserted document

print("Document Inserted with ID", post_id)
