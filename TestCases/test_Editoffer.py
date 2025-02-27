import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import Login
from PageObjects.EditOffer import OfferEdit
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from builtins import input


class Test_003_Editoffer:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_Editoffer(self,setup):
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

        self.offer = OfferEdit(self.driver)
        self.offer.clickOnListOffer()
        time.sleep(3)
        self.logger.info("******selected offer******")
        self.offer.clickOnEditOffer()
        time.sleep(5)

        ##edit client company field

        #subtitle_element = self.driver.find_element(By.NAME, self.txtSubtitle_name)
        self.offer.clickTitle("Reg")
        self.offer.clickSubTitle("test")

        ##promotional text
        self.offer = OfferEdit(self.driver)
        promo_text = self.offer.clickOnPromotionalText("Automation testing")

        ###terms
        Terms_text = self.offer.clickOnTerms("Buy one, get one")

        ###description
        Des_text = self.offer.clickOnDescription("50% cashback")

        ##tags
        tags = self.offer.clickOnTags("Milk")
        tags.send_keys(Keys.ENTER)
        time.sleep(5)

        ##product LOgo
        Logo = self.offer.clickOnProductLogo("https://rabble-res.cloudinary.com/image/upload/v1683035655/offer-content/soya-lista.png")
        time.sleep(2)
        ##Image1
        #Image = self.offer.ClickOnImage1("https://res.cloudinary.com/rabble-staging/image/upload/v1634549905/coke_product_image_uc6jky.png")
        #time.sleep(3)
        ##From Date
        Fromdate = self.offer.clickOnFromDate("2024-05-11 15:00")
        time.sleep(2)

        ##ToDate
        Todate = self.offer.clickOnToDate("2024-05-17 15:00")
        time.sleep(2)

        ##userredemption
        Userred = self.offer.clickOnUseredemption("10")

        ##totalRedemption
        totalred = self.offer.clickOnTotalredem("100")

        ##unlimiteUserredemption check
        #self.offer.UnlimitedUserredemCheck()
        time.sleep(2)

        ###single redemption per receipt
        self.offer.MultiRdptionPerReceipt()

        ###Budget
        budget = self.offer.OfferBudget("20")

        ###click on the country selector
        self.offer.clickOnCountry()

        ####select the country
        self.offer.clickOnCountryselect()
        time.sleep(2)

        ### To keep my window open
        #input("Press any key to close the browser window...")
        #self.driver.quit()

        ##click on offer dropdown

        self.offer.clickOnOffer()
        time.sleep(2)
        self.offer.clickOnOfferType()

        ###select offer

        self.offer.clickOnCashback("5")
        time.sleep(3)

        ##Enter Min total qty   (this will be disable for the single offers)
        #self.offer.clickOnTotalMinQty()

        ##enter product name
        product = self.offer.clickOnProductName("Avacado")

        ####enter line item
        lineitem = self.offer.clickOnReceiptLineItem("Milk")
        time.sleep(10)


        #Click on Save
        #self.offer.clickOnSave()
        time.sleep(5)





















