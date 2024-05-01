from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoFindElementByXpath:

    def locate_by_xpath(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)

        driver.maximize_window()
        sleep(2)

        login_box = driver.find_element(By.XPATH, "//input[@id='login-input']")
        login_box.send_keys('test@test.com')
        sleep(2)


if __name__ == '__main__':
    find_by_xpath = DemoFindElementByXpath()

    find_by_xpath.locate_by_xpath()