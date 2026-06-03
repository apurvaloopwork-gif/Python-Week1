file = open('file.txt','r')

f = file.readlines()

#print(f) 

newList=[]
for line in f:
  if line[:-1] == '\n':
   newList.append(line[:-1]) #Removes the \n
  else:
    newList.append(line)
    
  
print(newList)
file.close()