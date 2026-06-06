book={}
book['tom'] ={
  'name':'tom',
  'address':'1 street,Ny',
  'phone':98456974
}
book['claire'] ={
  'name':'claire',
  'address':'2 street,Ny',
  'phone':5321554
}

import json
# s=json.dumps(book)
# print(s)

# with open("demo1.json","w") as f:
#   f.write(s)
  
  
#read the json file

f=open("demo1.json","r")
s = f.read()
print(s)
