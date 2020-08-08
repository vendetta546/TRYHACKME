import requests
import json

path = "f"
value = ""
host = "https://10.10.112.87:3000/"

while 1:
	response = requests.get(host + path)
	dict_data =  json.loads(response.text)
	path = dict_data["next"]
	if path == "end":
		break
	value = value + dict_data["value"]


print(value)
