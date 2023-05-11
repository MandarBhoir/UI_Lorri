import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_SearchByCountry(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("india")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results in search_results:
            assert results.text == "India Security Press, Nashik, Maharashtra"
            break

    def test_CheckSearchCountByCountry(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("india")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        assert len(search_results) == 30

    def test_SearchByState(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results2 in search_results:
            if results2.text == "Khed, Pune, Maharashtra":
                print("Test Pass")
                break
            else: print("Test Fail")

    def test_CheckSearchCountByState(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        assert 30 == len(search_results)

    def test_SearchByCity(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("thane")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results3 in search_results:
            assert results3.text == "Thane, Thane, Maharashtra"
            break

    def test_CheckSearchCountByCity(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        assert 30 == len(search_results)

    def test_SearchByLessKeyword(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("th")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        if not search_results:
            print("Test pass")
        else:
            print("Test fail")

    def test_SearchByMoreKeyword(self):
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
            assert results.text == "Thane, Thane, Maharashtra"
            break

    def test_SearchByInvalid(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("Thane, Thane, Maharashtra")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        time.sleep(2)
        for results in search_results:
            assert results.text != "lokmanya nagar"
            break

    def test_SearchByNumber(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("123456")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        if not search_results:
            print("Test pass")
        else:
            print("Test fail")

    def test_SearchBySC(self):
        self.driver.find_element(By.ID, "custom-input-suggest-id").send_keys("!@#$%^&*()")
        search_results = self.driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']//ul[1]//li")
        if not search_results:
            print("Test pass")
        else:
            print("Test fail")












