# User models
# Pymongo connection

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["user"]

# Insert a document into the collection
mydict = { "name": "Vipin", "email": "vipinbhojwani@gmail.com" }
x = mycol.insert_one(mydict)
