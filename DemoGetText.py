from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
class Democlasstogettext:

    def locate_get_text(self):

        service =  ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://www.yatra.com/business")
        sleep(3)

        driver.maximize_window()
        sleep(1)

        text = driver.find_element(By.XPATH, "//p[@class='main-heading sme-text-center']").text
        print(f"text : {text}")

if __name__ == "__main__":

    obj_gettext = Democlasstogettext()
    obj_gettext.locate_get_text()