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

        # Create banner action
        self.createbanner = Banners(self.driver)
        self.createbanner.Clickonfeaturedbannerstab()
        time.sleep(5)
        self.createbanner.ClickOnCreatebannerbtn()
        time.sleep(2)
        self.createbanner.ClickOnnamefield("test")
        time.sleep(3)
        self.createbanner.ClickOnFromfield("2024-07-25 00:00")
        time.sleep(5)
        self.createbanner.ClickOnTofield("2024-08-25 00:00")
        time.sleep(5)
        self.createbanner.ClickOnWieght("1")
        time.sleep(5)
        self.createbanner.ClickOnCountrydrpdown()
        time.sleep(4)
        self.createbanner.SelectCountry()
        time.sleep(3)
        self.createbanner.ClickOnScope()
        time.sleep(4)
        self.createbanner.ClickOnManualreviewScope()
        body = setup.find_element(By.TAG_NAME, 'body')       # To close the scope menu
        ActionChains(setup).move_to_element(body).click().perform()
        time.sleep(3)
        self.createbanner.ClickOnURI("rabble://settings")
        time.sleep(3)
        self.createbanner.ClickImage("https://res.cloudinary.com/rabble-staging/image/upload/v1634549905/coke_product_image_uc6jky.png")
        time.sleep(2)
        self.createbanner.ClickOnSave()
        time.sleep(5)







