import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
#options = webdriver.ChromeOptions()

##Noting all the elements
class Receipt:
    Receiptbtn_xpath = "//a[@href='/dashboard/receipts?page=1&per_page=25']"
    slcreceiptfromlist_xpath = "//tbody//tr[1]//td[2]"  ##//tbody//tr[2]//td[2] ## //tbody//tr[last()-1]//td[2] selected the 1st receipt

    # select the dropdown(pending)
    pendingdrpdwn_xpath="//div[contains( @class , 'MuiSelect-select') and text()='PENDING']"   #click on dropdown
    approvedrpdwn_xpath = "//li[@data-value='APPROVED']"   # approve
    rejectdrpdwn_xpath = "//li[@data-value='REJECTED']"   # reject

    currenctdrpdwn_Id = "standard-select-currency"  ##//div[@id='standard-select-currency']"    #Currency dropdow
    SEKcurrency_xpath = "//li[@data-value='SEK']"
    EURcurrency_xpath = "//li[@data-value='EUR']"
    DKKcurrency_xpath = "//li[@data-value='DOK']"
    NOKcurrency_xpath = "//li[@data-value='NOR']"

    ####add offer manually
    Addoffer_xpath = "//button[normalize-space()='ADD OFFER']"
    Searchoffer_xpath="//button[@aria-label='Open']"##autosearch
    Cashback_xpath = "(//div[@data-testid='customInput']//input[@type='number'])[2]"
    Deletereceip_xapth ="//button[.='DELETE RECEIPT']"    ##delete receipt
    Deletepromtcomfirm_xpath= "//button[.='Delete']"     ##alert to confirm the delete a receipt
    Receiptshortcuts_xpath= "//button[.='SHORTCUTS']"
    Closeshortcuts_xapth= "//button[.='Close']"

    ##select the status for the manually added offer
    setstatus_xpath="(//em[normalize-space() = 'Set status'])"
    Adminofferapprove_xpath =  "(//li[@data-value='APPROVED'])[1]"

    ##Duplicate receipts show more
    duplicateshowmore_xpath = "//button[text()='SHOW MORE']"
    Userreceiptsshowmore_xpath ="(//button[text()='SHOW MORE'])[2]"

    Savereceipt_xpath ="//p[text()='SAVE']"
    # Save receipt




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clickonreceipttab(self):
        self.driver.find_element(By.XPATH, self.Receiptbtn_xpath).click()

    def clickonreceipt(self):
        self.driver.find_element(By.XPATH, self.slcreceiptfromlist_xpath).click()

    def clickOnpendingdrpdwn(self):
        self.driver.find_element(By.XPATH,self.pendingdrpdwn_xpath).click()

    def clickOnApproved(self):
        self.driver.find_element(By.XPATH, self.approvedrpdwn_xpath).click()

    def clickOnRejected(self):
        self.driver.find_element(By.XPATH, self.rejectdrpdwn_xpath).click()

    def clicOnCurrencydrpdwn(self):
        self.driver.find_element(By.ID, self.currenctdrpdwn_Id).click()
    def clickOnSEK(self):
        self.driver.find_element(By.XPATH, self.SEKcurrency_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.Savereceipt_xpath).click()

    def clickOnAddoffer(self):
        self.driver.find_element(By.XPATH, self.Addoffer_xpath).click()

    def clickOnAutoSearch(self):
        self.driver.find_element(By.XPATH, self.Searchoffer_xpath).click()

    def clickOnCashbackField(self, Cashback):
        self.driver.find_element(By.XPATH, self.Cashback_xpath).send_keys(Cashback)

    def clickOnsetstausForAdminOffers(self):
        self.driver.find_element(By.XPATH, self.setstatus_xpath).click()

    def clickonApproveforadminoffer(self):
        self.driver.find_element(By.XPATH, self.Adminofferapprove_xpath).click()

    def clickondeletereceipt(self):
        self.driver.find_element(By.XPATH, self.Deletereceip_xapth).click()

    def clickonconfirmToDeletReceipt(self):
        self.driver.find_element(By.XPATH, self.Deletepromtcomfirm_xpath).click()

    def clickOnshortcuts(self):
        self.driver.find_element(By.XPATH, self.Receiptshortcuts_xpath).click()

    def clickOncloseShortcuts(self):
        self.driver.find_element(By.XPATH, self.Closeshortcuts_xapth).click()

    def clickOnRejected(self):
        self.driver.find_element(By.XPATH, self.rejectdrpdwn_xpath).click()     ##reject the receipt

    def clickOnReceiptsShowMore(self):
        self.driver.find_element(By.XPATH, self.duplicateshowmore_xpath).click()

    def clickOnUserShowMore(self):
        self.driver.find_element(By.XPATH, self.Userreceiptsshowmore_xpath).click()














