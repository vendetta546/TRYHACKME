import requests
path = 'robots.txt'
host = 'http://10.10.241.214'
while(host is not ''):
    response = requests.get(host + path)
    print (response)
