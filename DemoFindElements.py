from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoFindElements:

    def locate_elements(self):

        service = ChromeService(executable_path= ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)
        driver.get('https://www.yatra.com/')
        sleep(2)

        driver.maximize_window()
        sleep(2)

        list_a = driver.find_elements(By.TAG_NAME, 'a')

        print(len(list_a))

        print([i.text for i in list_a])


if __name__ == "__main__":

    find_elements_1 = DemoFindElements()

    find_elements_1.locate_elements()
