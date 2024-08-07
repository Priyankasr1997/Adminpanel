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

class Test_005_Receiptreview:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_ReceipReview(self,setup):
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

        # Clickng on the receipt button
        self.receipt = Receipt(self.driver)
        self.receipt.Clickonreceipttab()
        time.sleep(5)

        self.receipt = Receipt(self.driver)
        self.receipt.clickonreceipt()
        # Get the total height of the page
        total_height = setup.execute_script("return document.body.scrollHeight")
        # Scroll to the middle of the page
        middle = total_height / 2
        setup.execute_script(f"window.scrollTo(0, {middle});")
        # Optionally, wait for a few seconds to see the result
        time.sleep(5)
