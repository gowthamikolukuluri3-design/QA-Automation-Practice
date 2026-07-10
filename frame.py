from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demoqa.com/frames?utm_source=chatgpt.com")
driver.maximize_window()
driver.implicitly_wait(12)
driver.switch_to.frame("frame1")
heading=driver.find_element(By.ID,"sampleHeading")
print(heading.text)

driver.switch_to.default_content()





driver.quit()
