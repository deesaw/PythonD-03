import pymongo
import random
import math
from pymongo import MongoClient
client=MongoClient()
dbs=client.stpp
coll=dbs.tepp
#db.students.drop()


types=['exam','quiz','homework','homework']
for i in range(0,10):
    scores=[]
    for j in range(0,4):
        scores.append({'type':types[j],'score':random.random()*100})
    class_id=math.floor(random.random()*501)
    record={'student_id':i,'scores':scores,'class_id':class_id}
    coll.insert(record)
print "done"
    
