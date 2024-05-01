from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class DemoFindElementByCSSSelector:

    def locate_by_css_selector(self):


        service = ChromeService(executable_path= ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')

        driver.maximize_window()
        sleep(2)

        login_box = driver.find_element(By.CSS_SELECTOR, "#login-input")
        login_box.send_keys("test@Test.com")

if __name__ == '__main__':
    find_by_css = DemoFindElementByCSSSelector()

    find_by_css.locate_by_css_selector()