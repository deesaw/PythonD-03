import pymongo

from pymongo import MongoClient
client=MongoClient()
dbs=client.database_names()#gets all the database names

for db in dbs:             #prints all the database names
    print (db)
