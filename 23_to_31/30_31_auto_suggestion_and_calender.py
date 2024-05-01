from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class DemoAutoSuggestion:

    def demo_autosuggestion(self):

        service = ChromeService(executavle_path = ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)

        driver.get("https://www.yatra.com")

        ele_departure = driver.find_element(By.XPATH, "// input[ @ id = 'BE_flight_origin_city']")
        ele_arrival = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        #click on departure box enter the "New Delhi" and enter
        ele_departure.click()
        sleep(2)
        ele_departure.send_keys("New Delhi")
        sleep(2)
        ele_departure.send_keys(Keys.ENTER)
        sleep(2)

        #Click on arrival, enter "New" keyword and get the list of webelement suggestion. iterate it and select one of them
        ele_arrival.click()
        sleep(2)
        ele_arrival.send_keys("New")
        sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print([res.text for res in search_result])
        #[res.click() for res in search_result if "New York (JFK)" in res.text]
        for res in search_result:
            if "New York (JFK)" in res.text:
                res.click()
                sleep(4)
                break

        #now we will select the date
        #1) first way is click on calender, select on perticuler date
        ele_departure_cale = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        ele_departure_cale.click()
        sleep(2)
        # ele_date_20_june = driver.find_element(By.XPATH,"//td[@id='20/06/2024']")
        # ele_date_20_june.click()
        # sleep(2)

        #2) second way is get the list of all the date web element and iterate it using loop and click perliure web element out of it
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD']")
        print("Lenth of the date list:", len(all_dates))
        for d in all_dates:
            if d.get_attribute("data-date") == "20/06/2024":
                d.click()
                sleep(2)
                break

if __name__ == "__main__":
    objAutosearch = DemoAutoSuggestion()
    objAutosearch.demo_autosuggestion()