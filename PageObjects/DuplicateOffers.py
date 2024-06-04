import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Duplicateoffer():
    MenuIndex = "//*[name()='svg'][@data-testid='MoreVertIcon']"   ###3 dots
    btnCreateduplicate = "//li[normalize-space()='Create Duplicate']"
    txtFromDate_xpath = "//input[@placeholder='yyyy-mm-dd hh:mm']"
    txtToDate_xpath = "(//input[@placeholder='yyyy-mm-dd hh:mm'])[2]"
    btnSave_xpath = "//button[normalize-space()='SAVE']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnListMenu(self):
        self.driver.find_element(By.XPATH, self.MenuIndex).click()

    def clickOnCreateDuplicate(self):
        self.driver.find_element(By.XPATH, self.btnCreateduplicate).click()

    def clickOnFromDate(self):
        self.driver.find_element(By.XPATH, self.txtFromDate_xpath)


    def clickOnFromDate(self, FromDate):
        self.driver.find_element(By.XPATH, self.txtFromDate_xpath).send_keys(FromDate)


    def clickOnToDate(self, ToDate):
        self.driver.find_element(By.XPATH, self.txtToDate_xpath).send_keys(ToDate)







