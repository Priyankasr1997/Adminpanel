import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from PageObjects.LoginPage import Login
from PageObjects.CreatOffer import CreateOffer
from Utilities.readProperties import RedConfig
from Utilities.readXML import ReadXML
from Utilities.customLogger import LogGen


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class Test_003_CreateOffer:

    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.parametrize("offer_data", ReadXML.get_offer_data("TestData/testdata.xml"))
    def test_CreateOffer(self, offer_data):

        driver = self.driver

        # ---------- OPEN URL ----------
        driver.get(self.webURL)
        self.logger.info("Opened URL")

        # ---------- LOGIN ----------
        lp = Login(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.ClickLogin()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CREATE OFFER']"))
        )

        # ---------- CREATE OFFER ----------
        offer = CreateOffer(driver)
        offer.clickOnCreateOffer()

        # ---------- CLIENT COMPANY ----------
        offer.select_client_company("1756: test company")

        # ---------- BASIC DETAILS (NO DUPLICATION) ----------
        offer.fill_basic_details(offer_data)

        # ---------- TAGS ----------
        tags = offer.clickOnTags()
        tags.send_keys("drinks")
        tags.send_keys(Keys.ENTER)

        # ---------- IMAGES ----------
        image_url = "https://rabble-res.cloudinary.com/image/upload/v1769767958/offer-content/Scalp-1.png"
        offer.clickOnProductLogo(image_url)
        offer.ClickOnImage1(image_url)

        # ---------- DATES ----------
        offer.clickOnFromDate("2024-05-11 00:00")
        offer.clickOnToDate("2024-05-17 00:00")

        # ---------- REDEMPTION (NO DUPLICATION) ----------
        offer.fill_redemption_details(offer_data)
        offer.UserUnlimitedredemCheck()
        offer.SingleRdptionPerReceipt()

        # ---------- STORES ----------
        offer.select_store("Rabble")

        # ---------- COUNTRY ----------
        offer.clickOnCountry()
        offer.clickOnCountryselect()

        # ---------- OFFER DETAILS (NO DUPLICATION) ----------
        offer.clickOnOffer()
        offer.clickOnOfferType()
        offer.fill_offer_details(offer_data)

        # ---------- SAVE ----------
        offer.clickOnSave()

        # ---------- VALIDATION CHECK ---------- #

        # Fail if validation errors are present
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CREATE OFFER']"))
        )

        # Fail if validation errors are present
        if offer.is_validation_error_present():
            errors = offer.get_validation_errors()
            assert False, f"Validation errors: {errors}"

        self.logger.info(f"Offer created successfully: {offer_data['title']}")