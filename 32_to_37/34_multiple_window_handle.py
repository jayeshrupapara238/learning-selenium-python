from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class DemoMultipleWindows:

    def handle_multiple_windows(self):

        service = ChromeService(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://www.yatra.com")
        driver.maximize_window()
        sleep(2)
        parent_handle = driver.current_window_handle
        print(f"Parent winodw handle:{parent_handle}")

        ele_spiritual = driver.find_element(By.XPATH, "//a[@title='Spiritual Divine Yatra']//img[@class='conta iner large-banner']")
        ele_spiritual.click()
        sleep(2)

        all_handle = driver.window_handles
        print(f"All the windows handel:{all_handle}")

        for handle in all_handle:
            if handle != parent_handle:
                spiritual_handle = handle
                driver.switch_to.window(handle)
                ele_Ayodhya = driver.find_element(By.XPATH,"//a[@href='https://www.yatra.com/india-tour-packages/holidays-in-ayodhya']//div[@class='Card']//span[contains(text(),'Book Now')]")
                ele_Ayodhya.click()
                sleep(2)
                #driver.close()
                #sleep(2)
                break

        # driver.switch_to.window(parent_handle)
        # driver.find_element(By.XPATH,"//span[normalize-space()='Hotels']").click()
        # sleep(5)

        all_handle = driver.window_handles
        print(f"All the windows handle:{all_handle}")

        for handle in all_handle:
            if (handle != parent_handle) and (handle != spiritual_handle):
                #print(f"handle now:{handle}")
                Ayodhya_handle = handle
                driver.switch_to.window(handle)

                ele_yourname = driver.find_element(By.XPATH,"//input[@id='name']")
                ele_yourname.send_keys("test")
                sleep(2)

                ele_emailID = driver.find_element(By.XPATH,"//input[@id='email']")
                ele_emailID.send_keys("text@text.com")
                sleep(2)

                ele_phoneno = driver.find_element(By.XPATH,"//input[@id='mobile']")
                ele_phoneno.send_keys("1111111111")
                sleep(2)

                ele_submit = driver.find_element(By.XPATH,"//button[@id='submit']")
                ele_submit.click()
                sleep(4)

                driver.close()
                sleep(3)

        driver.switch_to.window(spiritual_handle)
        driver.close()
        sleep(3)

        driver.switch_to.window(parent_handle)
        driver.close()
        sleep(3)

if __name__ == "__main__":

    objhandle = DemoMultipleWindows()
    objhandle.handle_multiple_windows()
