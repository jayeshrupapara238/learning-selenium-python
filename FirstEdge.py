from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import time

#service = EdgeService(executable_path='C:\\BrowserDriver\\msedgedriver.exe')
#driver = webdriver.Edge(service)

driver = webdriver.Edge()



driver.get('https://www.rvcacademy.com')
driver.maximize_window()
time.sleep(1)
print(driver.title)
time.sleep(1)
driver.close()