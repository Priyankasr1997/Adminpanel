import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import Login
from PageObjects.EditOffer import OfferEdit
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEditOffer:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        options = Options()
        options.add_experimental_option("detach", True)  # Keeps browser open
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        # Commented to keep browser open after test execution
        # self.driver.quit()

    def test_edit_offer(self):
        self.logger.info("****** Starting Edit Offer Test ******")
        self.driver.get(self.webURL)

        # Login
        lp = Login(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.ClickLogin()
        self.logger.info("****** Login successful ******")
        time.sleep(3)

        # Edit Offer
        offer = OfferEdit(self.driver)
        offer.clickOnListOffer()
        time.sleep(5)
        self.logger.info("****** Selected offer ******")

        offer.clickOnEditOffer()
        time.sleep(3)

        # Edit fields
        offer.clickTitle("Reg")
        offer.clickSubTitle("test")
        offer.clickOnPromotionalText("Automation testing")
        offer.clickOnTerms("Buy one, get one")
        offer.clickOnDescription("50% cashback")

        tags = offer.clickOnTags("Milk")
        tags.send_keys(Keys.ENTER)
        time.sleep(1)

        offer.clickOnProductLogo(
            "https://rabble-res.cloudinary.com/image/upload/v1683035655/offer-content/soya-lista.png")
        time.sleep(1)

        offer.clickOnFromDate("2024-05-11 15:00")
        offer.clickOnToDate("2024-05-17 15:00")

        offer.clickOnUseredemption("10")
        offer.clickOnTotalredem("100")

        # Handle checkboxes
        multi_redemp_locator = "//input[@name='multiRedemption']"
        unlimited_redemp_locator = "//input[@name='unlimitedRedemption']"
        single_redemp_locator = "//input[@name='singleRedemption']"

        # Managing redemption logic
        offer.manage_redemption_selection()

        # Verify the checkbox and radio buttons
        assert not (offer.is_element_selected(offer.unlimitedredemptioncheckbox_perperson_xpath) and
                    offer.is_element_selected(offer.rdobtn_multipleredem_perperson)), \
            "Both unlimited checkbox and multiple redemption radio button are selected!"

        assert not (offer.is_element_selected(offer.rdobtn_singleredem_perperson) and
                    offer.is_element_selected(offer.rdobtn_multipleredem_perperson)), \
            "Both single and multiple redemption radio buttons are selected!"

        #offer.OfferBudget("20")

        offer.clickOnCountry()
        offer.clickOnCountryselect()
        time.sleep(1)

        offer.clickOnOffer()
        time.sleep(1)
        #offer.clickOnOfferType()

        offer.clickOnCashback("5")
        time.sleep(1)

        offer.clickOnProductName("Avocado")
        offer.clickOnReceiptLineItem("Milk")
        time.sleep(2)

        # Save the offer
        offer.clickOnSave()

        self.logger.info("****** Edit Offer Test Completed ******")
        time.sleep(2)
