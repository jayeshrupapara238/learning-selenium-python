from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoHiddenElement:

    def demo_is_displayed(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        sleep(3)

        ele_toggle_button = driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']")
        ele_hidden = driver.find_element(By.XPATH, "//div[@id='myDIV']")

        sleep(1)
        print("Is hidden element displaying now:", ele_hidden.is_displayed())
        sleep(3)
        ele_toggle_button.click()
        sleep(2)
        print("After pressing toggle button, let's check hidden element is displaying:", ele_hidden.is_displayed())

    def demo_is_displayed_yatra(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver_1 = webdriver.Chrome(service = service)

        driver_1.get("https://www.yatra.com/hotels")
        driver_1.maximize_window()
        ele_room = driver_1.find_element(By.XPATH, "//span[normalize-space()='Room']")
        ele_room.click()
        sleep(2)

        ele_add_child = driver_1.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]")
        ele_add_child.click()
        sleep(2)

        ele_child_age = driver_1.find_element(By.XPATH, "//select[@class='ageselect']")
        print("Is child age element displing:", ele_child_age.is_displayed())
        sleep(2)

        ele_abs_child = driver_1.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]")

        ele_abs_child.click()
        sleep(2)
        #we will get error here because element will get removed from DOM once child number removed.
        print("After removing child element, check child age is displing:", ele_child_age.is_displayed())
        sleep(2)

if __name__ == "__main__":

    obj_hidden_ele = DemoHiddenElement()
    #obj_hidden_ele.demo_is_displayed()
    obj_hidden_ele.demo_is_displayed_yatra()