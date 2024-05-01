from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoExecuteJS:

    def execute_javascipt(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        # driver.get("https://www.rcvacademy.com/")
        # sleep(2)
        # ele_course = driver.find_element(By.XPATH, "//p[contains(text(),'Learn Test Automation, Manual Testing, ISTQB Certi')]")
        # ele_course.click()
        # sleep(2)

        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")
        sleep(12)
        ele_course = driver.execute_script("return document.getElementsByTagName('a')[78];")
        driver.execute_script("arguments[0].click();", ele_course)
        sleep(2)

if __name__ == "__main__":
    objExeJS = DemoExecuteJS()
    objExeJS.execute_javascipt()