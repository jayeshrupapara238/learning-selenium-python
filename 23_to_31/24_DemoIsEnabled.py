from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoIsEnabled:

    def element_enable_disable(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://training.openspan.com/login")
        sleep(2)

        ele_login_button = driver.find_element(By.XPATH,"//input[@id='login_button']")

        print("State of the login button element:", ele_login_button.is_enabled())

        if ele_login_button.is_enabled() != True:
            print("Login button is disable now, please enebale by adding text to user name and password")

            ele_username = driver.find_element(By.XPATH, "//input[@id='user_name']")
            ele_password = driver.find_element(By.XPATH, "//input[@id='user_pass']")

            ele_username.send_keys("aaaaaaa")
            sleep(1)
            ele_password.send_keys("ababababab")
            sleep(1)

            print("ckeck the state of the login button now:", ele_login_button.is_enabled())
            ele_login_button.click()
            sleep(1)

if __name__ == "__main__":
    objIsEnable = DemoIsEnabled()
    objIsEnable.element_enable_disable()
