#read Html file 
from bs4 import BeautifulSoup

with open("demo.html","r") as f:
  doc=BeautifulSoup(f,"html.parser")
   
# print(doc) 
# print(doc.prettify()) #Formatted code  


# tag=doc.title #Find the name by tag 
# print(tag)

tag=doc.title #Find the name by tag 
# print(tag.String)#Gives you the title name 

# tag.string ="Demo"#modfy tags
# print(tag.string)

#Find the all by tag name 

tags = doc.find_all("p")[0] #Access b tag inside p tag
# print(tags)
print(tags.findAll("b"))

