import pymongo

try:
    connection = pymongo.MongoClient("localhost",27017)
    database = connection["FirstDB"]
    collection = database["myCollection"]

    print("Connection is Successful")



except Exception as error:
    print(error)
