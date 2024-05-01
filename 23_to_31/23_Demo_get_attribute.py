from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Demo_get_attribute:

    def locate_ele(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://www.yatra.com/")
        sleep(2)

        ele_yatra_for_bussi = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack']")
        print("Value of attribute data trackcategary:", ele_yatra_for_bussi.get_attribute("data-trackcategory"))
        print('Value of attribute data-trackaction:', ele_yatra_for_bussi.get_attribute("data-trackaction"))
        print("Value of attribute herf:", ele_yatra_for_bussi.get_attribute("href"))
        print("Value of attribute data-trackvalue:", ele_yatra_for_bussi.get_attribute("data-trackvalue"))
        print("Value of attribute class:",ele_yatra_for_bussi.get_attribute("class"))

if __name__ == "__main__":
    obj_ele = Demo_get_attribute()
    obj_ele.locate_ele()