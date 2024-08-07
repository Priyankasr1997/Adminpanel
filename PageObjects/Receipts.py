import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#options = webdriver.ChromeOptions()

##Noting all the elements
class Receipt:
    Receiptbtn_xpath = "//a[@href='/dashboard/receipts?page=1&per_page=25']"
    slcreceiptfromlist_xpath = "//tbody//tr[1]//td[2]"  ##//tbody//tr[2]//td[2] ## //tbody//tr[last()-1]//td[2] selected the 1st receipt

    # select the dropdown(pending)
    pendingdrpdwn_xpath="// div[contains( @class , 'MuiSelect-select') and text()='PENDING']"   #click on dropdown
    approvedrpdwn_xpath = "//li[@data-value='APPROVED']"   # approve
    rejectdrpdwn_xpath = "//li[@data-value='REJECTED']"   # reject

    currenctdrpdwn_xath = "//div[@id='standard-select-currency']"    #Currency dropdow
    SEKcurrency_xpath = "//li[@data-value='SEK']"
    EURcurrency_xpath = "//li[@data-value='EUR']"
    DKKcurrency_xpath = "//li[@data-value='DOK']"
    NOKcurrency_xpath = "//li[@data-value='NOR']"
    Savereceipt_xpath = "//p[text()='SAVE']"                  # Save receipt




    def __init__(self, driver):
        self.driver = driver

    def Clickonreceipttab(self):
        self.driver.find_element(By.XPATH, self.Receiptbtn_xpath).click()

    def clickonreceipt(self):
        self.driver.find_element(By.XPATH, self.slcreceiptfromlist_xpath).click()


