import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import Login
from PageObjects.CreatOffer import CreateOffer
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Test_003_CreateOffer:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_CreateOffer(self,setup):
        self.driver = setup
        self.driver.get(self.webURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("******Login successfully******")
        time.sleep(6)

    ##clickon on the create offer button

        self.offer = CreateOffer(self.driver)
        self.offer.clickOnCreateOffer()
        time.sleep(5)

    ##Client company field

        element = setup.find_element(By.XPATH, "//input[@placeholder='Client Company']")

        # Click on the input element to activate the dropdown
        element.click()

        # Wait for the dropdown options to appear (assuming 6 seconds is sufficient)
        time.sleep(6)

        # Send keys to the input element to search for a company (e.g., '1756: test company')
        element.send_keys("1756: test company")

        # Press Enter to select the first option (assuming pressing Enter selects the first option)
        element.send_keys(Keys.RETURN)
        ## Title Field
        self.offer.clickTitle("Reg test")
        ##subtitle
        self.offer.clickSubTitle("RT")
        ##promotion
        self.offer.clickOnPromotionalText("Hi")
        ##terms
        self.offer.clickOnTerms("welcome")
        ##description
        self.offer.clickOnDescription("Rabble")

        ##tags
        tags_input = self.offer.clickOnTags()  # Now clickOnTags() returns the tags input field WebElement
        tags_input.send_keys("drinks") # Send keys to the tags input field
        tags_input.send_keys(Keys.ENTER)
        time.sleep(4)

        ##product logo
        self.offer.clickOnProductLogo("https://res.cloudinary.com/rabble-staging/image/upload/v1647599417/frankful_fryst_offer_list_zdj1sc.jpg")
        time.sleep(5)
        self.offer.ClickOnImage1("https://res.cloudinary.com/rabble-staging/image/upload/v1647599417/frankful_fryst_offer_list_zdj1sc.jpg")

        ##From Date
        self.offer.clickOnFromDate("2024-05-11 00:00")

        ##ToDate
        self.offer.clickOnToDate("2024-05-17 00:00")


        ##Useredemption
        self.offer.clickOnUseredemption("10")

        ##Totalredem
        self.offer.clickOnTotalredem("20")

        ####add budget
        self.offer.OfferBudget("10")

        ##Unlimiteduserredemption checkbox
        self.offer.UserUnlimitedredemCheck()

        ##Multiple redemption per receipt
        #self.offer.MultiRdptionPerReceipt()      //this check cant be enabled if the unlimiteduserredemption checkbox is active

        ##Single redemption per receipt
        self.offer.SingleRdptionPerReceipt()

        ##Store
        Stores = self.offer.clickOnStores()
        #Stores.click()
        Stores.send_keys("Rabble")
        time.sleep(5)
        # 2nd Store Entry
        Stores.send_keys(Keys.ENTER)
        Stores.send_keys("Or")
        time.sleep(5)
        Stores.send_keys(Keys.ENTER)
        time.sleep(3)

        ##click on country drpdown
        self.offer.clickOnCountry()

        ###select the country
        self.offer.clickOnCountryselect()

        ##select offer(single, volume, ,.....)

        Offer = setup.find_element(By.XPATH, "(//div[@id='standard-select-currency'])[2]")
        Offer.click()  ##offer type
        OfferType = setup.find_element(By.XPATH, "//li[@data-value='Volume']")
        OfferType.click()  # Single,Volume,Bundle

        self.offer.clickOnCashback("10")                         ##enterFixed cashback
        self.offer.clickOnTotalMinQty("2")                      ###enter min total qty
        self.offer.clickOnProductName("Panettone")              ##product name
        self.offer.clickOnReceiptLineItem("Risotto")              ####line item
        #self.offer.clickOnSave()
        time.sleep(5)
        #Save = setup.find_element(By.XPATH, "//button[normalize-space()='SAVE']")     ###save offer
        #Save.click()
        time.sleep(10)
        self.logger.info("******Offer Created successfully******")


































