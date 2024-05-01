from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class DemoSwitchIframe:

    def handle_iframe(self):

        service = ChromeService(executable_path= ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

        driver.maximize_window()
        sleep(2)

        # #swith frame by frame element locator
        # ele_parentiframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
        # driver.switch_to.frame(ele_parentiframe) # switched to main frame

        # #switch frame by ID
        # driver.switch_to.frame("iframewrapper")

        #switch from by name
        driver.switch_to.frame("iframeResult")

        #switch frame by index
        driver.switch_to.frame(0)

        ele_signup = driver.find_element(By.XPATH,"//a[@href='https://profile.w3schools.com/sign-up?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fdefault.asp']")
        ele_signup.click()
        sleep(10)




if __name__ == "__main__":
    objIframe = DemoSwitchIframe()
    objIframe.handle_iframe()