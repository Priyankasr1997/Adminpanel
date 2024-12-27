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
    verifyuser_xpath ="//ul//li[3]" ##click on verify button
    verifyuserconfirmpromt_xpath = "//button[text()='VERIFY']"

    ##Migrate user
    migrateuser_xpath="//ul//li[4]"         ##click on migrate user button
    countrydrpdwn_xpath = "//div[@id='standard-select-currency']"   ##click on arrow to select the dropdown
    selectcountry_xpath= "//li[@data-value='DK']"   #select country  //li[@data-value='SE, Fi, NOK']>> all countries
    migrateprompt_xpath = "//button[text()='MIGRATE']"  #confirm prompt

    ##delete user
    deleteuser_xpath = "//ul//li[5]"    ##select delect button
    deletecomfirmprompt_xpath = "//button[text()='Delete']"  ##confirm prmt to delete user

    ## Search users
    search_id = "input-search-header"    ## click on search field




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # User tab click action
    def ClickOnUserTab(self):
        self.driver.find_element(By.XPATH, self.usertab_xpath).click()

    # click on user
    def ClickOnuser(self):
        self.driver.find_element(By.XPATH, self.selectuser_xpath).click()

    # click on options
    def clickOnOptions(self):
        self.driver.find_element(By.XPATH, self.options_xpath).click()

    # click on freeze and unfreeze user button
    def ClickOnFreezeUser(self):
        self.driver.find_element(By.XPATH, self.freezeuser_xpath).click()

    # click on prompt to yes to freeze user
    def ConfirmPromt(self):
        self.driver.find_element(By.XPATH, self.confirmpromt_xpath).click()

    # click on prompt to yes to unfreeze user
    def ClickOnUnfreezeUserprompt(self):
        self.driver.find_element(By.XPATH, self.unfreeze_xpath).click()

    # click on disable and enable user button
    def ClickOndisableUser(self):
        self.driver.find_element(By.XPATH, self.disableuser_xpath).click()

    def ClickOnDisableConfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.disableconfirmpromt_xpath).click()

    def ClickOnEnableConfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.enableuser_xpath).click()

    def ClicOnVerifyUser(self):                                # verify user
        self.driver.find_element(By.XPATH, self.verifyuser_xpath).click()

    def ClickOnVerifyuserConfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.verifyuserconfirmpromt_xpath).click()

    def ClickOnMigrateUser(self):
        self.driver.find_element(By.XPATH, self.migrateuser_xpath).click()

    def ClickOnCountrydropdown(self):
        self.driver.find_element(By.XPATH, self.countrydrpdwn_xpath).click()

    def ClickOnSelectcountry(self):
        self.driver.find_element(By.XPATH, self.selectcountry_xpath).click()

    def ClickOnMigrateConfirm(self):
        self.driver.find_element(By.XPATH, self.migrateprompt_xpath).click()

    def ClickOnDeleteUser(self):
        self.driver.find_element(By.XPATH, self.deleteuser_xpath).click()

    def ClickOnDeleteconfirmPrompt(self):
        self.driver.find_element(By.XPATH, self.deletecomfirmprompt_xpath).click()


    def ClickOnSearch(self):
        search = self.driver.find_element(By.ID, self.search_id)
        search.click()
        return search


















