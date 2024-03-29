import pymongo

try:
    connection = pymongo.MongoClient("localhost",27017)
    database = connection["FirstDB"]
    collection = database["myCollection"]

    print("Connection is Successful")



except Exception as error:
    print(error)


data = {"name" : "Benjamin","age" : 23, "Hobby" : "Python Programming"}

try:
    collection.insert_one(data)
    print("Data are inserted")

except Exception as error:
    print(error)


