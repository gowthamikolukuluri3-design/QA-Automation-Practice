from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com?utm_source=chatgpt.com")
driver.find_element(By.XPATH,"//a[text()='Digest Authentication']").click()
alert=driver.switch_to.alert()

alert.dismiss()


driver.quit()