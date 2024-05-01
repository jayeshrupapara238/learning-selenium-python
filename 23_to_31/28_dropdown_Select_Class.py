from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
class DemoDropdowmSelectClass:

    def dropdown_select(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://demo.guru99.com/test/newtours/register.php")

        ele_dropdown_country = driver.find_element(By.XPATH,"//select[@name='country']")

        drop_country = Select(ele_dropdown_country)

        drop_country.select_by_index(0)
        sleep(2)
        drop_country.select_by_value("ALGERIA")
        sleep(2)
        drop_country.select_by_visible_text("ANGOLA")
        sleep(2)

if __name__ == "__main__":

    objDropdown = DemoDropdowmSelectClass()
    objDropdown.dropdown_select()