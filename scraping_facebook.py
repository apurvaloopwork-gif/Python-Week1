from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F")
emailid = driver.find_element(By.NAME, "email")
emailid.send_keys("hometvs1982@gmail.com")
password = driver.find_element(By.NAME, "Pass")
password.send_keys("Hometvs@1982")
password.send_keys(Keys.RETURN)
time.sleep(10)
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Apurva")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

print(driver.page_source)

driver.quit()
