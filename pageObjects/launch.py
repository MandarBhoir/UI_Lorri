import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/User/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.lorri.in/")
driver.find_element(By.ID, "custom-input-suggest-id").send_keys("India")
search_results = driver.find_elements(By.XPATH,"//div[@id='react-autowhatever-1']//ul[1]//li")
time.sleep(2)
print(len(search_results))

for results in search_results :
    assert "India Security Press, Nashik, Maharashtra" == results.text
    break
driver.close()


service_obj = Service("/Users/User/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.lorri.in/")
driver.find_element(By.ID, "custom-input-suggest-id").send_keys("Maharashtra")
search_results = driver.find_elements(By.XPATH,"//div[@id='react-autowhatever-1']//ul[1]//li")
time.sleep(2)
print(len(search_results))

for results in search_results :
    assert "Khed, Pune, Maharashtra" == results.text
    break
driver.close()
