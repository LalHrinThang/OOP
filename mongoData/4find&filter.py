import pymongo

connection = pymongo.MongoClient("localhost",27017)

database = connection["FirstDB"]

collection = database["Students_Info"]


data = [
    {"_id" : 5,"name" : "Benny" , "age":22,"class":13},
    {"_id" : 6,"name" : "Zane" , "age" : 22, "class": 14},
    {"_id" : 7,"name" : "Benjamin Lala","age" : 15,"class": 12}
]
query1 = {"_id":6}
query2 = {"_id":{"$gt":4}}
query3 = {"name":{"$gt":"C"}}
try:
    data_query1 = collection.find(query1)
    for d in data_query1:
        print(d)
    print("This is only one finding query\n")
    data_query2 = collection.find(query2)
    for d in data_query2:
        print(d)
    print("This is multiple Query \n")

    data_query3 = collection.find(query3)
    for d in data_query3:
        print(d)    
    print("This is also multiple Query")
    # result = collection.insert_many(data)
    # print(result.inserted_id)
    # _ids = collection.find().distinct("_id")

    # print(_ids)
    # _name = collection.find().distinct("name")
    # print(_name)

    # data_finding = collection.find_one()
    # print(data_finding)
    # print("This is find_one method \n")
    # data_finding = collection.find()
    # for i in data_finding:
    #     print(i)
    # print("This is find(all) method\n")
    # data_finding = collection.find({},{"name":0})
    # for j in data_finding:
    #     print(j)
    # print("This is selective find method \n")

    # data_finding = collection.find({},{"name":1})
    # for k in data_finding:
    #     print(k)
    # print("\n This is selective finding method")

    #QUERY Method
except Exception as error:
    print(error)

