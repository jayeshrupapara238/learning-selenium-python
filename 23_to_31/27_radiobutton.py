from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
class Demo_radio_button:

    def select_radio(self):
        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://demo.guru99.com/test/radio.html")
        sleep(2)

        ele_radio1 = driver.find_element(By.XPATH, "//input[@id='vfb-7-1']")
        ele_radio2 = driver.find_element(By.XPATH, "//input[@id='vfb-7-2']")
        ele_radio3 = driver.find_element(By.XPATH, "//input[@id='vfb-7-3']")

        print("Check first radio button:", ele_radio1.is_selected())
        ele_radio1.click()
        sleep(2)
        print("Check first radio button:", ele_radio1.is_selected())

        ele_radio2.click()
        sleep(2)
        print("Check first radio button:", ele_radio1.is_selected())
        ele_radio3.click()
        sleep(2)




if __name__ == "__main__":
    objradio = Demo_radio_button()
    objradio.select_radio()