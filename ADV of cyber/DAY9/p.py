#!/usr/bin/python3
import requests
host = 'http://10.10.241.214'
port = '3000'
nextRoute = ''
flag = ''
while(nextRoute != 'end'):
    response = requests.get(host + ':' + port + '/' + nextRoute)
    parsed = response.json()
    nextRoute = parsed['next']
    if(nextRoute != 'end'):
        flag += parsed['value']
print(flag)
