import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) 
clist=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for location in clist:
        picture='http'+location["file"].split('http')[1]
        file.write(location["stitle"]+","+location["address"][5:8]+","+location["longitude"]+","+location["latitude"]+","+picture+"\n")