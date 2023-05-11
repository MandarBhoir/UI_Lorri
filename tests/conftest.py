import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    global service_obj
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/Users/User/Documents/chromedriver.exe")
    elif browser_name == "firefox":
        #firefox browser invocation code
        print("Firefox")
    elif browser_name == "IE":
        print("IE Driver")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://www.lorri.in/")
    request.cls.driver = driver
    yield
    driver.close()

