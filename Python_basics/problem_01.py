## Problem 1: FizzBuzz, NBFC edition (10 min)

# Write a function `loan_status(month)` that takes a number from 1 to 30 (the day of the month a borrower's EMI is due) and returns:

# - `"On time"` if the day is divisible by 5
# - `"Grace period"` if the day is divisible by 3
# - `"Grace period (on time bonus)"` if divisible by both 3 and 5
# - `"Late"` otherwise

def loan_status(day):
   if (day%5==0):
      print(f"day:{day} - On time")
      
   elif(day%3==0):
     print(f"day:{day} - Grace period")
     
   elif(day%3==0 and day%5==0):
     print(f"day:{day} - Grace period, One time bonus")
     
   else:
     print(f"day:{day} - Late!")
     
     
#-----------This asks for specific day and gives the output-------------------
# d=int(input("Enter the day of borrower's EMI is due-"))
#  loan_status(d)

#------------This keeps asking for input till day 30-----------------------------
# for i in range(1,31):
#   d=int(input("Enter the day of borrower's EMI is due-"))
#   loan_status(d)

#---------------This gives output fromday 1-30---------------------------------   
for i in range(1,31):
  loan_status(i)