from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoFindElementByClassAndTag:

    def locate_element_by_class_tag(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        sleep(3)

        driver.maximize_window()
        sleep(1)

        #text_box = driver.find_element(By.CLASS_NAME, 'email-login-box')
        text_box = driver.find_element(By.TAG_NAME, 'input')

        text_box.send_keys('test@test.com')
        sleep(2)


if __name__ == "__main__":
    locate_obj = DemoFindElementByClassAndTag()
    locate_obj.locate_element_by_class_tag()

