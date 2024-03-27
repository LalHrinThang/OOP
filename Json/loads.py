import json

myJson = """{

"name" : "Lal Hrin Thang",
"age" : 22,
"hobby" : ["Programming","Teaching","WebDevelopment"]
}"""

myData = json.loads(myJson)

print(type(myData))

print(myData)