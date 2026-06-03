import csv

header =["Name","Age","City"]
data =[["Aman",17,"Jaipur"],
        ["Bhavaesh",19,"Mumbai"],
        ["Chirag",16,"Jodhpur"]
      ]

with open("people.csv","w",newline ="") as fp:
  wr = csv.writer(fp)
  wr.writerow(header)
  wr.writerows(data) 
  
print("CSV file written successfully")