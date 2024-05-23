from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

user_input = input("Enter 1 to search for a product: ")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_query = "headphones"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

main_div = driver.find_element(By.CLASS_NAME, 's-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row')

products = main_div.find_elements(By.CLASS_NAME, 'puisg-row')


driver.quit()