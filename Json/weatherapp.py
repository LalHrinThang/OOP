import json
import requests


key = "00bf089a8a417ecbd90cbc613148a637"

url = "https://api.openweathermap.org/data/2.5/weather?appid=00bf089a8a417ecbd90cbc613148a637&q="

city = input("Please enter your city : ")

newUrl = url+city #&q_______location


jsonData = requests.get(newUrl).json()

#dict type
#print(jsonData)
print(jsonData["coord"])