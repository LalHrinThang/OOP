import json
import requests


key = "00bf089a8a417ecbd90cbc613148a637"

url = "https://api.openweathermap.org/data/2.5/weather?appid=00bf089a8a417ecbd90cbc613148a637&q="

city = input("Please enter your city : ")

newUrl = url+city
jsonData = requests.get(newUrl).json()
print(type(jsonData))
print(jsonData)

data =json.dumps(jsonData,indent=5)

print(type(data))

print(data)