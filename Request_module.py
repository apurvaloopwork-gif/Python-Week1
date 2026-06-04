import requests

r = requests.get("https://loopwork-in.onrender.com")

# print(r.text)

with open("demo2.html",'w',encoding="utf-8") as f:
  f.write(r.text)