from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get('https://www.rvcacademy.com')
driver.maximize_window()
print(driver.title)
driver.close()