import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class User:
    usertab_xpath="//a[@href='/dashboard/users?page=1&per_page=25']"   ## click on users module
    selectuser_xpath = "//tbody//tr[1]//td[2]"    ##select user
    options_xpath = "//button[text()='OPTIONS']"  ##click on options button

    ##Freeze user
    freezeuser_xpath="//li[@role='menuitem']"  ##select freezeuser button
    confirmpromt_xpath="//button[text()=' FREEZE ACCOUNT']"  #confirm or say yes to freeze user
    unfreeze_xpath = "//button[text()='UNFREEZE ACCOUNT']"   #confirm or say yes to Unfreeze user

    ##Disable user
    disableuser_xpath="//ul//li[2]"       ## select disable
    disableconfirmpromt_xpath = "//button[text()='DISABLE ACCOUNT']"   ###confirm or say yes to disable user
    enableuser_xpath="//button[text()='ENABLE ACCOUNT']"               ###Confiirm promt to Enable user

    ##verify User
    verifyuser_xpath ="//ul//li[3]"       ##verify user


    ##Migrate user
    migrateuser_xpath="//ul//li[4]"         ##click on migrate user button
    countrydrpdwn_xpath = "//div[@id='standard-select-currency']"   ##click on arrow to select the dropdown
    selectcountry_xpath= "//li[@data-value='DK']"   #select country  //li[@data-value='SE, Fi, NOK']>> all countries

    deleteuser_xpath = "//ul//li[5]"        ##delete user

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def ClickOnUserTab(self):
        self.driver.find_element(By.XPATH, self.usertab_xpath).click()
    def ClickOnuser(self):
        self.driver.find_element(By.XPATH, self.selectuser_xpath).click()

    def clickOnOptions(self):
        self.driver.find_element(By.XPATH, self.options_xpath).click()

    def ClickOnFreezeUser(self):
        self.driver.find_element(By.XPATH, self.freezeuser_xpath).click()

    def ConfirmPromt(self):
        self.driver.find_element(By.XPATH, self.confirmpromt_xpath).click()

    def UnfreezeUserprompt(self):
        self.driver.find_element(By.XPATH, self.unfreeze_xpath).click()

    def ClickOndisableUser(self):
        self.driver.find_element(By.XPATH, self.disableuser_xpath).click()

    def DisableConfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.disableconfirmpromt_xpath).click()

    def EnableConfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.enableuser_xpath).click()
    def ClicOnVerifyUser(self):
        self.driver.find_element(By.XPATH, self.verifyuser_xpath).click()













