import pymongo

connection = pymongo.MongoClient("localhost",27017)

database = connection["FirstDB"]

collection = database["Students_Info"]


data = {"_id" : 4,"name" : "Benjamin Aaron" , "age":22,"class":12}

try:
    _ids = collection.find().distinct("_id")

    print(_ids)
    _name = collection.find().distinct("name")
    print(_name)
except Exception as error:
    print(error)

