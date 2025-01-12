import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class Banners:
    Bannerstab_xpath = "//p[text()='Featured Banners']"
    Createbannerbtn_xpath = "//button[text()='Create Banner']"
    Nameinputfield_xpath = "//input[@id='outlined-basicname']"
    Frominputfield_xpath ="//input[@name='from']"
    Toinputfield_xpath ="//input[@name='to']"
    weightinputfield_xpath ="//input[@name='weight']"
    countrydrpdown_xpath ="//div[@id='outlined-basiccountry']"
    selectcountry_xpath = "//li[@data-value='SE']"      #FI, NO, DK for other countries
    scopedropdown_xpath = "//div[@id='scopes-multiple-select']"
    cashbackscope_xpath = "//li[@data-value='cashback-list']"
    Manualviewscope_xpath = "//li[@data-value='manual-review']"
    URIinputfiled_xpath = "//input[@name='URI']"
    imageinputfiled_xpath = "//input[@name='image']"
    Savebutton_xpath = "//button[@type='submit']"
    selectbannerfromlist_xpath = "//tbody//tr[2]//td"    # to select the 2nd record //tbody//tr[3]//td....
    EditButton_xpath = "//button[text()='EDIT']"
    DeleteButton_xpath = "//button[text()='DELETE']"
    Deleteprompt_xpath = "//button[text()='Delete']"




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clickonfeaturedbannerstab(self):
        self.driver.find_element(By.XPATH, self.Bannerstab_xpath).click()

    def ClickOnCreatebannerbtn(self):
        self.driver.find_element(By.XPATH, self.Createbannerbtn_xpath).click()

    def ClickOnnamefield(self, Name):
        self.driver.find_element(By.XPATH, self.Nameinputfield_xpath).send_keys(Name)

    def ClickOnFromfield(self, FromDate):
        self.driver.find_element(By.XPATH, self.Frominputfield_xpath).send_keys(FromDate)

    def ClickOnTofield(self,ToDate):
        self.driver.find_element(By.XPATH, self.Toinputfield_xpath).send_keys(ToDate)

    def ClickOnWieght(self, Weight):
        self.driver.find_element(By.XPATH, self.weightinputfield_xpath).send_keys(Weight)

    def ClickOnCountrydrpdown(self):
        self.driver.find_element(By.XPATH, self.countrydrpdown_xpath).click()

    def SelectCountry(self):
        self.driver.find_element(By.XPATH, self.selectcountry_xpath).click()

    def ClickOnScope(self):
        self.driver.find_element(By.XPATH, self.scopedropdown_xpath).click()

    def ClickOnManualreviewScope(self):
        self.driver.find_element(By.XPATH, self.Manualviewscope_xpath).click()

    def ClickOnCashbackscope(self):
        self.driver.find_element(By.XPATH, self.cashbackscope_xpath).click()

    def ClickOnURI(self, URI):
        self.driver.find_element(By.XPATH, self.URIinputfiled_xpath).send_keys(URI)

    def ClickImage(self, Image):
        self.driver.find_element(By.XPATH, self.imageinputfiled_xpath).send_keys(Image)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.Savebutton_xpath).click()

    def ClickOnBanner(self):
        self.driver.find_element(By.XPATH, self.selectbannerfromlist_xpath).click()

    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, self.EditButton_xpath).click()

    def ClickOnDelete(self):
        self.driver.find_element(By.XPATH, self.DeleteButton_xpath).click()

    def ClickOnDeleteCnfirmprompt(self):
        self.driver.find_element(By.XPATH, self.Deleteprompt_xpath).click()














