from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME,"radius").click()
print("message")
driver.quit()
