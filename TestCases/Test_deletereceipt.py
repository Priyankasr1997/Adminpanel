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
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # browser will not automatically close


class Test_005_Receipt:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_Addoffer(self,setup):
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

        self.deletereceipt = Receipt(self.driver)
        self.deletereceipt.Clickonreceipttab()
        time.sleep(7)


        self.deletereceipt = Receipt(self.driver)
        self.deletereceipt.clickonreceipt()
        time.sleep(5)
        self.deletereceipt.clickondeletereceipt()
        time.sleep(5)
        self.deletereceipt.clickonconfirmToDeletReceipt()
        time.sleep(10)
