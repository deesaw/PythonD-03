from pymongo import MongoClient

## access databases using attribute style access on MongoClient instances
client = MongoClient()

db = client.test_database

## If your database name is such that using attribute style access won’t work (like test-database),
## you can use dictionary style access instead

#db = client['test-database']

print(db)