from selenium import webdriver
import pytest
from PageObjects.LoginPage import Login  # Assuming you have LoginPage for login
from Utilities.readProperties import RedConfig

# Command-line options for pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. Default is Chrome.")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

# Session-scoped browser setup (shared across all tests)
@pytest.fixture(scope="session")
def setup(browser):
    print(f"Setting up the browser: {browser}")

    # Browser setup
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)

    # Perform login only once
    perform_login(driver)

    yield driver  # Provide driver to tests

    driver.quit()
    print("Browser closed after session.")

# Function to handle login logic separately
def perform_login(driver):
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()

    driver.get(webURL)
    login_page = Login(driver)
    login_page.setUserName(username)
    login_page.setPassword(password)
    login_page.ClickLogin()
    print("Logged in successfully once for the session.")

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
