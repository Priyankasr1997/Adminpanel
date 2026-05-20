import pytest
from PageObjects.LoginPage import Login
from PageObjects.DuplicateOffers import Duplicateoffer
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver


@pytest.mark.usefixtures("setup")
class Test_003_Duplicateoffer:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_dupOffer(self, setup):
        self.driver = setup
        self.driver.get(self.webURL)
        self.driver.maximize_window()
        self.logger.info("Navigated to Web URL")

        # Login Steps
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("****** Login successful ******")

        # Duplicate Offer Actions
        self.duplicate = Duplicateoffer(self.driver)
        self.logger.info("Navigated to Duplicate Offer Section")

        self.duplicate.clickOnListMenu()
        self.logger.info("Clicked on List Menu")

        self.duplicate.clickOnCreateDuplicate()
        self.logger.info("Clicked on Create Duplicate")

        self.duplicate.clickOnFromDate("2025-05-11 00:00")
        self.logger.info("Entered From Date")

        self.duplicate.clickOnToDate("2025-05-17 00:00")
        self.logger.info("Entered To Date")

        # Uncomment when ready to save
        # self.duplicate.clickOnSave()
        # self.logger.info("Clicked on Save Button")

        self.logger.info("****** Duplicate Offer Test Completed ******")
        #self.driver.quit()

