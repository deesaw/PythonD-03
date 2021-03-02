#inserting more docs
import datetime
import pymongo
from pymongo import MongoClient
client=MongoClient()
#dbs=client.database_names()
db=client.pyex #db pyex
coll=db.pycoll
new_posts = [{"author": "Gandhi",
"text": "An Autobiography!",
"tags": ["bulk", "insert"],
"date": datetime.datetime(2019, 10, 09, 11, 14)
},
{"author": "Richard",
"title": "The Words of Gandhi",
"text": "interesting!",
"date": datetime.datetime(2019, 10, 08, 10, 34)

}]
coll.insert(new_posts)
print coll.count()
s=coll.find({})
for ss in s:
    print ss

