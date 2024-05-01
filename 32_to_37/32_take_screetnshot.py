from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class DemoTakeScreenshot:

    def capture_screenshot(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        sleep(2)

        ele_continue = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        ele_continue.click()
        sleep(2)
        ele_continue.screenshot(".\\screenshot\\continue.png")
        sleep(2)

        driver.save_screenshot(".\\screenshot\\error_login.png")
        driver.get_screenshot_as_file(".\\screenshot\\eoor_login_1.png")


if __name__ == "__main__":
    objScreenshot = DemoTakeScreenshot()
    objScreenshot.capture_screenshot()