import allure
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Running tests in ************* Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Running tests in ************* Firefox Browser")
    else:
        driver=webdriver.Chrome()
        print("Running tests in ************* Chrome Browser")


    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



# ***************** Pytest HTML Report Configuration ********************
def pytest_metadata(metadata):
    metadata["Project Name"] = "Yatra Website Automation"
    metadata["Module Name"] = "Landing Page"
    metadata["Tester"] = "Naveenkumar T"

# ***************** Pytest Allure Report Configuration ********************


@pytest.fixture()
def log_on_failure(request,setup):
    driver = setup
    yield
    item = request.node
    if item.rep_call.failed:
       allure.attach(driver.get_screenshot_as_png(), "Failed Screenshot", attachment_type=allure.attachment_type.PNG)



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep