from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

wait=WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((By.ID,"username"))
).send_keys("tomsmith")

wait.until(EC.element_to_be_clickable((By.ID,"password"))
).send_keys("SuperSecretPassword!")

wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
).click()

print("Login Sucessful")

result=wait.until(EC.element_to_be_clickable((By.ID,"flash"))
).text

assert "You logged into a secure area!" in result

driver.quit()

