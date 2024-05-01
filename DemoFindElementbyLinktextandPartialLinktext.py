from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class FindElementByLinkText:

    def locate_by_linktext(self):

        service = ChromeService(executable_path= ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get('https://www.yatra.com/')
        sleep(1)
        driver.maximize_window()
        sleep(3)
        #text_link = driver.find_element(By.LINK_TEXT, "Yatra for Business")

        text_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for Busine")

        text_link.click()

        sleep(5)


if __name__ == '__main__':

    find_obj = FindElementByLinkText()

    find_obj.locate_by_linktext()
