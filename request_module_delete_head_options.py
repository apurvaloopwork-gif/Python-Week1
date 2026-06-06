import requests

r1 = requests.delete('https://httpbin.org/delete')
r2 = requests.head('https://httpbin.org/get')
r3 = requests.options('https://httpbin.org/get')


# print(r1.text)
#print(r2.headers)

print(r3.headers)
