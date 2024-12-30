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
from selenium.webdriver.common.action_chains import ActionChains
from PageObjects.Receipts import Receipt
from PageObjects.Users import User
from PageObjects.FeatureBanners import Banners
from PageObjects.EditBanners import EditBanner

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Test_005_featuredbanners:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_Createbanners(self, setup):
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

        # Edit banner action
        self.editbanner = EditBanner(self.driver)
        self.editbanner.Clickonfeaturedbannerstab()
        time.sleep(5)
        self.editbanner.ClickOnBanner()
        time.sleep(2)
        self.editbanner.ClickOnEdit()
        time.sleep(4)
        Name_element = self.editbanner.ClickOnname("Testing")
        time.sleep(3)

        Edit_From = self.editbanner.ClickOnFrom("2024-08-25 00:00")
        time.sleep(3)
        Edit_To = self.editbanner.ClickOnTo("2024-10-29 00:00")
        time.sleep(3)
        self.editbanner.ClickOncountry()
        time.sleep(2)
        self.editbanner.SelectCountry()
        time.sleep(4)
        Edit_URI = self.editbanner.ClickOnURI("https://www.rabble.se")
        time.sleep(5)
