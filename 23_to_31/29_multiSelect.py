from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class DemoMultiSelect:

    def demo_multiselect(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://output.jsbin.com/osebed/2")

        ele_fruits = driver.find_element(By.XPATH, "//select[@id='fruits']")

        select_fruit = Select(ele_fruits)

        select_fruit.select_by_index(0)
        sleep(2)
        select_fruit.select_by_value("apple")
        sleep(2)
        select_fruit.select_by_visible_text("Grape")
        sleep(2)

        select_fruit.deselect_by_index(0)
        sleep(2)

        select_fruit.deselect_all()
        sleep(4)


if __name__ == "__main__":
    objMulti = DemoMultiSelect()
    objMulti.demo_multiselect()