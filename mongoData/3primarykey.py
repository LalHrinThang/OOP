import pymongo
try:
    connection = pymongo.MongoClient("localhost",27017)

    database = connection["FirstDB"]

    collection = database["Students_Info"]

    print("Connection Successful")
except Exception as error:
    print(error)


insert_data = {"_id" : 3,"name" : "Aaron","Class" : 10}

try:
    result = collection.insert_one(insert_data)

    print(f'Data are inserted successfully \n ID : {result.inserted_id}')

except Exception as error:
    print(error)




