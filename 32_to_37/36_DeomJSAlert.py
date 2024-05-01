from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
class DemoJSalert:

    def handel_JS_ppoup(self):

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver =webdriver.Chrome(service=service)

        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        sleep(2)

        driver.switch_to.frame("iframeResult")

        ele_tryit = driver.find_element(By.XPATH, "//button[normalize-space()='Try it']")
        ele_tryit.click()
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(4)

        ele_tryit.click()
        sleep(4)
        driver.switch_to.alert.dismiss()
        sleep(4)

        ele_tryit.click()
        sleep(4)
        print(f"Alert text is : {driver.switch_to.alert.text}")
        driver.switch_to.alert.send_keys("HELLO")
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(4)

if __name__ == "__main__":

    objalert = DemoJSalert()
    objalert.handel_JS_ppoup()
