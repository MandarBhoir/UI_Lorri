import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_SearchByCountry(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("india")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results in search_results:
            assert "India Security Press, Nashik, Maharashtra" == results.text
            break

    def test_SearchByState(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results2 in search_results:
            assert "Khed, Pune, Maharashtra" == results2.text
            break

    def test_SearchByCity(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("thane")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results3 in search_results:
            assert "Thane, Thane, Maharashtra" == results3.text
            break

    def test_SearchBylesskeyword(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("thane")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        if not search_results:
            print("Test pass")
        else:
            print("Test fail")

    def test_SearchBymorekeyword(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("Ulhas")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for result in search_results:
            assert "Ulhas" in result.text

    def test_SearchByExactMatch(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("Thane, Thane, Maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results in search_results:
            assert "Thane, Thane, Maharashtra" == results.text
            break

    def test_SearchByinvalid(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("Thane, Thane, Maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results in search_results:
            assert "lokmanya nagar" == results.text
            break









