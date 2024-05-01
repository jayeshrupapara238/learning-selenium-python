from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
#driver = webdriver.Chrome(executable_path = "C:\\BrowserDriver\\chromedriver.exe")


service = ChromeService(executable_path = 'C:\\BrowserDriver\\chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('https://www.rvcacademy.com')

driver.maximize_window()

time.sleep(1)
print(driver.title)

time.sleep(1)
driver.close()