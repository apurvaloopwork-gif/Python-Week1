#Scraped laptops from 1-20 and saved it in a folder in html format from amazon.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
query = "laptop"
file = 0
driver = webdriver.Firefox()
for i in range(1, 20):

    driver.get(
        f"https://www.amazon.in/s?k={query}&page={i}&xpid=nq6IOvusPwDEr&crid=M0REBQ460KN&qid=1780751264&sprefix=laptop%2Caps%2C231&ref=sr_pg_2"
    )

    time.sleep(2)

    elems = driver.find_elements(
        By.CLASS_NAME,
        "puis-card-container"
    )
    print(f"{len(elems)} items found on page {i}")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data_selenium_build/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
    
    file += 1

driver.quit()