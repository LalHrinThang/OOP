import json

myJson = {
    "name" : "Lal Hrin Thang",
    "age" : 22,
    "pro" : ["Web Developer","Data Scientist","Python Programmer"]
}
myJson2 = {
    "name" : "Lal Hrin Thang",
    "age" : 22,
    "pro" : ["Web Developer","Data Scientist","Python Programmer"]
}
print("With dump and load method\n")
with open ("2data.json","w") as dataFile:
    data = json.dump(myJson,dataFile)
print(type(data))
print(data)

with open ("2data.json","r") as rdataFile:
    data = json.load(rdataFile)
print(type(data))
print("{data}\n")

print("With dumps and loads method\n")
jData = json.dumps(myJson2)
print(type(jData))

pData = json.loads(jData)

print(type(pData))