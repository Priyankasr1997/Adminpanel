from re import search

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from PageObjects.LoginPage import Login
from PageObjects.Users import User
from Utilities.readProperties import RedConfig
from Utilities.customLogger import LogGen

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # browser will not automatically close


class Test_005_Receipt:
    webURL = RedConfig.getAppUrl()
    username = RedConfig.getUseremail()
    password = RedConfig.getPassword()
    logger = LogGen.loggen()

    def test_Verifyuser(self, setup):
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

        # Navigate to the User tab and search
        self.userverify = User(self.driver)
        self.userverify.ClickOnUserTab()
        time.sleep(7)

        search_box = self.userverify.ClickOnSearch()
        search_box.send_keys("786653")
        search_box.send_keys(Keys.ENTER)
        time.sleep(4)

        # Locate the records

        records = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tr//td[2]"))
         )
            if records:
                # Click on the first record
                records[0].click()
                self.logger.info("Successfully clicked on the first record.")
            else:
                self.logger.warning("No records found.")

        except TimeoutException:
            self.logger.error("Timeout occurred while waiting for the records.")
        except NoSuchElementException:
            self.logger.error("No matching records were found.")
        finally:
            self.driver.quit()
