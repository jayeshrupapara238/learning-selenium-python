from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
class DemoCheckbox:

    def checkbox_is_selected(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://demo.guru99.com/test/radio.html")
        sleep(2)

        ele_checkbox_1 = driver.find_element(By.XPATH, "//input[@id='vfb-6-0']")
        ele_checkbox_2 = driver.find_element(By.XPATH, "//input[@id='vfb-6-1']")
        ele_checkbox_3 = driver.find_element(By.XPATH, "//input[@id='vfb-6-2']")

        print("Check the first checkbox:", ele_checkbox_1.is_selected())
        print("Check the second checkbox:", ele_checkbox_2.is_selected())
        print("Check the thrird checkbox:", ele_checkbox_3.is_selected())

        ele_checkbox_1.click()
        sleep(2)
        ele_checkbox_2.click()
        sleep(2)
        ele_checkbox_3.click()
        sleep(2)

        print("Check the first checkbox:", ele_checkbox_1.is_selected())
        print("Check the second checkbox:", ele_checkbox_2.is_selected())
        print("Check the thrird checkbox:", ele_checkbox_3.is_selected())


if __name__ == "__main__":

    objCheckbox = DemoCheckbox()
    objCheckbox.checkbox_is_selected()