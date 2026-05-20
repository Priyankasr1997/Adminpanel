import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage import Login
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_Login:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.fixture(scope="class")
    def setup(self, request):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(self.webURL)
        request.cls.driver = driver
        yield driver
        driver.quit()

    def test_homepageTitle(self):
        self.logger.info("******Test_001_Login******")
        self.logger.info("******Verify homepage******")
        act_title = self.driver.title
        assert act_title == "Rabble", f"Expected title 'Rabble' but got '{act_title}'"
        self.logger.info("******Home title page is passed******")

    def test_login(self):
        self.logger.info("******Starting login test******")
        lp = Login(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.ClickLogin()