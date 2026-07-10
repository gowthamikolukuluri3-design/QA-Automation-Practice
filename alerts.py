from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()

alert=driver.switch_to.alert
print(alert.text)

alert.accept()
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
alert.dismiss()
result=driver.find_element(By.ID,"result").text

assert "You clicked: Cancel" in result
driver.quit