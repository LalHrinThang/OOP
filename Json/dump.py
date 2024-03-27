import json

myJson = {
"name" : "Lal Hrin Thang",
"age" : 16,
"Work" : "Student"
}

with open ("data.json","w") as jsonData:
    json.dump(myJson,jsonData)

