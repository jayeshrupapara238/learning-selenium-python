from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

class DemoMouseHover:

    def event_mouse_hover(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://www.yatra.com")
        driver.maximize_window()
        sleep(2)

        ele_myaccount = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        ele_more = driver.find_element(By.XPATH, "//span[@class='more-arr']")

        achain = ActionChains(driver)

        achain.move_to_element(ele_myaccount).perform()
        sleep(2)

        achain.move_to_element(ele_more).perform()
        sleep(2)

        ele_tarin = driver.find_element(By.XPATH, "//span[normalize-space()='Trains']")
        ele_tarin.click()
        sleep(5)

if __name__ == "__main__":

    objmouse = DemoMouseHover()
    objmouse.event_mouse_hover()