from selenium import webdriver
import pytest
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # browser will not automatically close

# Browser setup fixture
@pytest.fixture
def setup(request, browser):
    print(f"Setting up the browser: {browser}")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    request.cls.driver = driver
    yield driver
    driver.quit()

# Command-line options for pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. Default is Chrome.")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Hook for adding environment info to HTML report
def pytest_configure(config):
    if not hasattr(config, 'slaveinput'):
        config._metadata = {
            'Project Name': 'Rabble',
            'Module Name': 'Login',
            'Tester': 'Priyanka'
        }
    print("pytest_configure called, metadata added.")

# Hook for modifying the environment info in HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    print("pytest_metadata called, metadata modified.")

# Fixture to keep the browser open after test execution
#
#@pytest.fixture(scope="function", autouse=True)
#def keep_browser_open():
 #   yield
  #  input("Press any key to close the browser window...")
#options.add_experimental_option("detach", True)  # browser will not automatically close