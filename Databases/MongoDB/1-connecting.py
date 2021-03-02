from pymongo import MongoClient
client = MongoClient()        # Connects to default host and port


#client = MongoClient('localhost', 27017)             ## We can also specify the host and port explicitly
#client = MongoClient('mongodb://localhost:27017/')   ## MongoDB URI format

print(client)