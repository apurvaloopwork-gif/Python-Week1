#locating_single
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

query="laptop"
driver = webdriver.Chrome()
driver.get(f"https://www.amazon.in/s?k={query}&crid=1TG737BU0EYOC&sprefix=laptop%2Caps%2C265&ref=nb_sb_noss_2")

elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")  #Found data through element
# print(elem.text)
# print(elem.get_attribute("outerHTML")) #Gives Outer HTML
print(f"{len(elems)} items found")
for elem in elems:
  print(elem.text)

time.sleep(2)
driver.close()
