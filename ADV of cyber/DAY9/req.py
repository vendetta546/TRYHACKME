import requests
url = "http://10.10.169.100:3000/"
response =  requests.get(url)
data = response.json()
flag = ""
while data['next'] != "end":
    flag += data['value']
    response = requests.get(url+data['next'])
    data = response.json()
print(flag)
