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

    def test_Migrateuser(self,setup):
        self.driver = setup
        self.driver.get(self.webURL)
        self.driver.maximize_window()
        self.logger.info("Navigating to Login Page")

        # Login action

        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("******Login successfully******")
        time.sleep(6)

        # verify migrate user
        self.usermigrate = User(self.driver)  # User is class name in the pageobject
        self.usermigrate.ClickOnUserTab()
        time.sleep(5)
        search = self.usermigrate.ClickOnSearch()
        search.send_keys("787016")  # 786359 unverified user
        search.send_keys(Keys.ENTER)

        # Wait for the table to load and locate all matching records
        records = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements(By.XPATH, "//tr//td[2]")  # Retrieves all matching elements
        )

        if records:
            # Click the first record
            records[0].click()
            time.sleep(5)
        else:
            print("No records found.")
            time.sleep(15)