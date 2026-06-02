#Functions
#Block of statement that perform specific tasks and we could use it over again 


def addTwo (x):
  return x+2

def subtractTwo(number):
  return number -2

def sqr(x):
  return x*x

# print(addTwo(4))
# print(subtractTwo(4))


#print(sqr(2))


def calc_sum(a,b):
    sum=a+b
    print(sum)

#calc_sum(80,100) #Function Call


#Avg of 3 numbers

def calc_avg(a,b,c):
  sum=a+b+c
  avg=sum/3
  print(avg)
  
  
#calc_avg(5,5,5)

#Write a function to get the length of list

def print_len(list):
  print(len(list))
  
cities = ['Delhi','Mumbai','Pune','chennai']

#print_len(cities)


#Function to convert USD into INR 

def converter(usd_val):
  inr_val = usd_val * 95.30
  print(usd_val,"USD =",inr_val,"INR")
  
#converter(25)


#Recursion 
#When a function calls itself repeatedly

#Write a recurssive function which prints n to 1 backwards

def show(n):
  if(n==0):
    return 
  print(n)
  show(n-1)
  
#show(10)

#Factorial function

def fact(n):
  if(n==0 or n == 1):
    return 1
  else:
    return n * fact(n-1)
  

  
print(fact(5))