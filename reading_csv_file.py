import csv

with open("people.csv","r") as fp:
  rd = csv.reader(fp)
  for row in rd:
    print(row)
    
print("Csv file read successfully")