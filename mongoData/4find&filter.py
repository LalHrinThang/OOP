import pymongo

connection = pymongo.MongoClient("localhost",27017)

database = connection["FirstDB"]

collection = database["Students_Info"]


data = [
    {"_id" : 5,"name" : "Benny" , "age":22,"class":13},
    {"_id" : 6,"name" : "Zane" , "age" : 22, "class": 14},
    {"_id" : 7,"name" : "Benjamin Lala","age" : 15,"class": 12}
]

try:
    # result = collection.insert_many(data)
    # print(result.inserted_id)
    _ids = collection.find().distinct("_id")

    print(_ids)
    _name = collection.find().distinct("name")
    print(_name)
except Exception as error:
    print(error)

