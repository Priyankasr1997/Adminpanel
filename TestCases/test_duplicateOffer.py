import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import Login
from PageObjects.DuplicateOffers import Duplicateoffer
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Test_003_Duplicateoffer:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_dupOffer(self,setup):
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

        self.duplicate = Duplicateoffer(self.driver)
        self.duplicate.clickOnListMenu()

        self.duplicate.clickOnCreateDuplicate()

        ##From Date
        self.duplicate.clickOnFromDate("2024-05-11 00:00")

        ##ToDate
        self.duplicate.clickOnToDate("2024-05-17 00:00")

        ##To save the offer
        #self.duplicate.clickOnSave()

