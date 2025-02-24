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
from selenium.webdriver.support.ui import Select

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
        time.sleep(10)

    ##clickon on the create offer button

        self.offer = CreateOffer(self.driver)
        self.offer.clickOnCreateOffer()
        time.sleep(6)
     #####CHECK
    ##Client company field

        element = setup.find_element(By.XPATH, "//input[@placeholder='Client Company']")
        time.sleep(2)

        # Click on the input element to activate the dropdown
        element.click()
        time.sleep(2)
        # Wait for the dropdown options to appear (assuming 6 seconds is sufficient)


        # Send keys to the input element to search for a company (e.g., '1756: test company')
        element.send_keys("1756: test company")
        time.sleep(5)

        # Press Enter to select the first option (assuming pressing Enter selects the first option)
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.logger.info("******Client company******")
        ## Title Field
        self.offer.clickTitle("Reg test")
        self.logger.info("******Title******")
        ##subtitle
        self.offer.clickSubTitle("RT")
        self.logger.info("****** Subtitle ******")
        ##promotion
        self.offer.clickOnPromotionalText("Hi")
        self.logger.info("****** promotional text ******")
        ##terms
        self.offer.clickOnTerms("welcome")
        self.logger.info("****** Terms ******")
        ##description
        self.offer.clickOnDescription("Rabble")
        self.logger.info("****** Description ******")


        ##tags
        tags_input = self.offer.clickOnTags()  # Now clickOnTags() returns the tags input field WebElement
        tags_input.send_keys("drinks") # Send keys to the tags input field
        tags_input.send_keys(Keys.ENTER)
        time.sleep(4)
        self.logger.info("****** Tags ******")


        ##product logo
        self.offer.clickOnProductLogo("https://res.cloudinary.com/rabble-staging/image/upload/v1647599417/frankful_fryst_offer_list_zdj1sc.jpg")
        time.sleep(5)
        self.offer.ClickOnImage1("https://res.cloudinary.com/rabble-staging/image/upload/v1647599417/frankful_fryst_offer_list_zdj1sc.jpg")
        self.logger.info("****** Images ******")

        ##From Date
        self.offer.clickOnFromDate("2024-05-11 00:00")
        self.logger.info("****** From Date ******")


        ##ToDate
        self.offer.clickOnToDate("2024-05-17 00:00")
        self.logger.info("****** To date ******")


        ##Useredemption
        self.offer.clickOnUseredemption("10")
        self.logger.info("****** User redemptions ******")


        ##Totalredem
        self.offer.clickOnTotalredem("20")
        self.logger.info("****** Total redemptions ******")


        ####add budget
        self.offer.OfferBudget("10")
        self.logger.info("****** Budget ******")


        ##Unlimiteduserredemption checkbox
        self.offer.UserUnlimitedredemCheck()
        self.logger.info("****** unlimited in user ******")


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
        Stores.send_keys(Keys.DOWN)  # Move to 1 suggestion
        Stores.send_keys(Keys.ENTER)
        time.sleep(3)
        self.logger.info("****** selected stores ******")


        ##click on country drpdown
        self.offer.clickOnCountry()
        self.logger.info("****** country dropdown******")
        ###select the country
        self.offer.clickOnCountryselect()
        time.sleep(2)
        self.logger.info("****** selected country ******")

        self.offer.clickOnOffer()
        time.sleep(2)
        self.offer.clickOnOfferType()
        self.logger.info("****** offer type selected******")
        self.offer.clickOnCashback("10")                         ##enterFixed cashback
        self.offer.clickOnTotalMinQty("2")                      ###enter min total qty
        self.offer.clickOnProductName("Panettone")              ##product name
        self.offer.clickOnReceiptLineItem("Risotto")              ####line item
        #self.offer.clickOnSave()
        time.sleep(10)
        self.logger.info("******Offer Created successfully******")


































