import requests

#Get requests
#This will pass key and key values to given url
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.json())