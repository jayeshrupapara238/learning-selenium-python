from selenium import webdriver
#from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

#service = FirefoxService(executable_path = 'C:\\BrowserDriver\\geckodriver.exe')
#driver = webdriver.Firefox(service = service)
driver = webdriver.Firefox()
driver.get('https://www.rvcacademy.com')

driver.maximize_window()
time.sleep(1)

print(driver.title)
time.sleep(1)

driver.close()