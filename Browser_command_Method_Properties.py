from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class BrowserMethodsProperties:

    def browser_methods_properties(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get('https://www.yatra.com/')
        sleep(2)

        print(driver.title)
        print(driver.current_url)
        driver.maximize_window()
        sleep(2)

        driver.minimize_window()
        sleep(2)
        driver.maximize_window()

        driver.fullscreen_window()
        sleep(2)

        driver.maximize_window()
        sleep(2)

        driver.find_element(By.XPATH, "//a[@title='Offers']").click()
        sleep(2)

        driver.back()
        sleep(2)

        driver.forward()
        sleep(2)

        driver.refresh()
        sleep(2)

        driver.quit()


if __name__ == "__main__":

    browser_command = BrowserMethodsProperties()
    browser_command.browser_methods_properties()