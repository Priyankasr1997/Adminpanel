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
from PageObjects.Receipts import Receipt
from PageObjects.Users import User

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Test_005_Receipt:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_Freezeuser(self, setup):
        self.driver = setup
        self.driver.get(self.webURL)
        self.driver.maximize_window()
        self.logger.info("Navigating to Login Page")
        time.sleep(4)

        # Login action
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("Login successful")
        time.sleep(5)

        # User freeze action
        self.userfreeze = User(self.driver)
        self.userfreeze.ClickOnUserTab()
        time.sleep(5)
        self.userfreeze.ClickOnuser()
        time.sleep(5)
        self.userfreeze.clickOnOptions()
        time.sleep(3)
        self.userfreeze.ClickOnFreezeUser()
        time.sleep(4)
        self.userfreeze.ConfirmPromt()
        time.sleep(5)

        # Verify freeze action

        self.logger.info("User freeze action completed successfully")

        self.driver.refresh()
        time.sleep(4)
        self.userfreeze.clickOnOptions()
        time.sleep(3)
        self.userfreeze.ClickOnFreezeUser()
        time.sleep(3)
        self.userfreeze.ClickOnUnfreezeUserprompt()
        time.sleep(3)
        self.logger.info("Unfreezed successful")



