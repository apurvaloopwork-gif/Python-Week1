import csv

def message_template(name):
  return f"Hii {name} We are AI agency for practical operators can we have your 10 minutes this week?\n Call us 1800-200-456"



with open("gyms.csv","r") as gp:
  rd = csv.reader(gp)
  for row in rd:
    gym_name=row[0]
    
    message = message_template(gym_name)
    
print(message)