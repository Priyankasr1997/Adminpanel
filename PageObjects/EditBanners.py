import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.FeatureBanners import Banners

from selenium.webdriver.support import expected_conditions as EC


class EditBanner:
    Bannerstab_xpath = "//p[text()='Featured Banners']"
    Createbannerbtn_xpath = "//button[text()='Create Banner']"
    Nameinputfield_xpath = "//input[@id='outlined-basicname']"
    Frominputfield_xpath = "//input[@name='from']"
    Toinputfield_xpath = "//input[@name='to']"
    weightinputfield_xpath = "//input[@name='weight']"
    countrydrpdown_xpath = "//div[@id='outlined-basiccountry']"
    selectcountry_xpath = "//li[@data-value='FI']"  # FI, NO, DK for other countries
    scopedropdown_xpath = "//div[@id='scopes-multiple-select']"
    cashbackscope_xpath = "//li[@data-value='cashback-list']"
    Manualviewscope_xpath = "//li[@data-value='manual-review']"
    URIinputfiled_xpath = "//input[@name='URI']"
    imageinputfiled_xpath = "//input[@name='image']"
    Savebutton_xpath = "//button[@type='submit']"
    selectbannerfromlist_xpath = "//tbody//tr[1]//td"  # to select the 2nd record //tbody//tr[3]//td....
    EditButton_xpath = "//button[text()='EDIT']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clickonfeaturedbannerstab(self):
        self.driver.find_element(By.XPATH, self.Bannerstab_xpath).click()

    def ClickOnBanner(self):
        self.driver.find_element(By.XPATH, self.selectbannerfromlist_xpath).click()

    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, self.EditButton_xpath).click()

    def ClickOnname(self, Name):
        Edit_name = self.driver.find_element(By.XPATH, self.Nameinputfield_xpath )
        Edit_name.send_keys(Keys.CONTROL + "a")
        Edit_name.send_keys(Keys.DELETE)
        Edit_name.send_keys(Name)
        Edit_name.click()
        return Edit_name

    def ClickOnFrom(self, From):
        Edit_From = self.driver.find_element(By.XPATH, self.Frominputfield_xpath )
        Edit_From.send_keys(Keys.CONTROL + "a")
        Edit_From.send_keys(Keys.DELETE)
        Edit_From.send_keys(From)
        Edit_From.click()
        return Edit_From

    def ClickOnTo(self, To):
        Edit_To = self.driver.find_element(By.XPATH, self.Toinputfield_xpath )
        Edit_To.send_keys(Keys.CONTROL + "a")
        Edit_To.send_keys(Keys.DELETE)
        Edit_To.send_keys(To)
        Edit_To.click()
        return Edit_To

    def ClickOncountry(self):
        self.driver.find_element(By.XPATH, self.countrydrpdown_xpath).click()

    def SelectCountry(self):
        self.driver.find_element(By.XPATH, self.selectcountry_xpath).click()


    def ClickOnweight(self, Weight):
        Edit_weight = self.driver.find_element(By.XPATH, self.Nameinputfield_xpath )
        Edit_weight.send_keys(Keys.CONTROL + "a")
        Edit_weight.send_keys(Keys.DELETE)
        Edit_weight.send_keys(Weight)
        Edit_weight.click()
        return Edit_weight

    def ClickOnScopedrpdown(self):
        self.driver.find_element(By.XPATH, self.scopedropdown_xpath).click()

    def ClickOnManualreviewScope(self):
        self.driver.find_element(By.XPATH, self.Manualviewscope_xpath).click()

    def ClickOnCashbackscope(self):
        self.driver.find_element(By.XPATH, self.cashbackscope_xpath).click()


    def ClickOnURI(self, URI):
        Edit_URI = self.driver.find_element(By.XPATH, self.URIinputfiled_xpath )
        Edit_URI.send_keys(Keys.CONTROL + "a")
        Edit_URI.send_keys(Keys.DELETE)
        Edit_URI.send_keys(URI)
        Edit_URI.click()
        return Edit_URI

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.Savebutton_xpath).click()


