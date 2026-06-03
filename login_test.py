from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

time.sleep(3)

if "Logged In Successfully" in driver.page_source:
    print("LOGIN TEST PASSED")
else:
    print("LOGIN TEST FAILED")

input("Press Enter to close browser...")
driver.quit()