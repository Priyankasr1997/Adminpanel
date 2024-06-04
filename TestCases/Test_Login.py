import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("******Test_001_Login******")
        self.logger.info("******Verify homepage******")
        self.driver = setup
        self.driver.get(self.webURL)
        options = Options()
        options.add_experimental_option("detach", True)
        act_title = self.driver.title
        if act_title == "Rabble":
            assert True
            self.driver.close()
            self.logger.info("******Home title page is passed******")
        else:
            #self.driver.close()
            assert False

    def test_login(self, setup):
            options = Options()
            options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(self.webURL)
            self.lp = Login(self.driver)
            time.sleep(5)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            self.logger.info("******Login successfully******")




