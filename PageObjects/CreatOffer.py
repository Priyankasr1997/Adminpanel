import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)  # browser will not automatically close

class CreateOffer:
    #adding all the locatores for the create offer page
    btnCreateOffer_xpath = "//button[normalize-space()='CREATE OFFER']"      #"//*[@id='root']/div[6]/main/div/div[1]/div/div/div/div[2]/button"
    autoSearch_Clientcompany_xpath = "//input[@placeholder='Client Company']"
    time.sleep(3)
    txtTitle_id = "outlined-basic"
    txtSubtitle_name = "subtitle"
    txtPromotional_xpath = "(//textarea[@name='textarea'])[1]"
    txtTerms_xpath = "(//textarea[@name='textarea'])[2]"
    txtDescription_xpath = "(//textarea[@name='textarea'])[3]"
    txtTags_xpath = "//input[@id='tags-standard']"
    txtProduct_Logo_xpath = "//input[@name='logoUrl']"
    txtProduct_Image1_name = "images_0"
    txtFromDate_xpath = "//input[@placeholder='yyyy-mm-dd hh:mm']"
    txtToDate_xpath = "(//input[@placeholder='yyyy-mm-dd hh:mm'])[2]"
    txtUser_Redemption_xpath = "//input[@name='redemptionPerson']"
    txtTotal_Redemption_xpath = "//input[@name='redemptionTotal']"
    chbUser_redemption_name = "//input[@name='redemptionPersonCheckbox']"  ###User unlimited redemption per person
    rdobtn_multipleredem_perperson = "/input[@name='limitation'][1]"    ##multile redemption per person
    unlimit_total_redem = " //input[@name='redemptionTotalCheckbox']"       ####total unlimited redemption
    rdobtn_singleredem_perperson = "/input[@name='limitation'][2]" ###single redemption per persion
    txtbudget_name = "budget"
    radiobtnUsereEligible_Multieredem_perReciept = "//input[@name='limitation']"
    radiobtnUsereEligible_Singleredem_perReciept = "(//input[@name='limitation'])[2]"
    txtStores_xpath = "//input[@placeholder='Stores (Brands)']"
    drpdwnCountry_xpath = "(//div[@id='standard-select-currency'])[1]"
    lsSelect_country = "//li[@data-value='FI']"
    txtTargeted_group_xpath = "//*[@id='mui-89']"
    drpoffer_xpath = "//div[@id='standard-select-currency'][2]" ##select dropdown
    drpofferType_xpath = "//li[@data-value='Volume']"
    txtCashback_xpath = "//input[@name='offerMechanismCashback']"
    txtTotal_Minqty_xpath = "//input[@name='minProductQuantity']"
    txtProductName_xpath = "//input[@name='productName_0']"
    txtReceipt_LineItem_xpath = "(//input[@type='text'])[16]"
    btnSave_xpath = "//button[normalize-space()='SAVE']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCreateOffer(self):
        self.driver.find_element(By.XPATH, self.btnCreateOffer_xpath).click()

    def clickClientCompany(self):
        self.driver.find_element(By.XPATH, self.autoSearch_Clientcompany_xpath).click()

    def clickTitle(self, Title):
        edit_title = self.driver.find_element(By.ID, self.txtTitle_id)
        edit_title.send_keys(Title)

    def clickSubTitle(self, Subtitle):
        self.driver.find_element(By.NAME, self.txtSubtitle_name).send_keys(Subtitle)

    def clickOnPromotionalText(self, Promotional):
        self.driver.find_element(By.XPATH, self.txtPromotional_xpath).send_keys(Promotional)

    def clickOnTerms(self, Terms):
        self.driver.find_element(By.XPATH, self.txtTerms_xpath).send_keys(Terms)

    def clickOnDescription(self, Description):
        self.driver.find_element(By.XPATH, self.txtDescription_xpath).send_keys(Description)

    #def clickOnTags(self):
     #   self.driver.find_element(By.XPATH, self.txtTags_xpath).click()
    def clickOnTags(self):
        tags_input = self.driver.find_element(By.XPATH, self.txtTags_xpath)
        tags_input.click()  # Click on the tags input field
        return tags_input

    def clickOnProductLogo(self, Image):
        self.driver.find_element(By.XPATH, self.txtProduct_Logo_xpath).send_keys(Image)


    def ClickOnImage1(self, Image1):
        self.driver.find_element(By.NAME, self.txtProduct_Image1_name).send_keys(Image1)

    def clickOnFromDate(self, FromDate):
        self.driver.find_element(By.XPATH, self.txtFromDate_xpath).send_keys(FromDate)

    def clickOnToDate(self, ToDate):
        self.driver.find_element(By.XPATH, self.txtToDate_xpath).send_keys(ToDate)

    def clickOnUseredemption(self, UserRedem):
        self.driver.find_element(By.XPATH, self.txtUser_Redemption_xpath).send_keys(UserRedem)


    def clickOnTotalredem(self, TotalRedem):
        self.driver.find_element(By.XPATH, self.txtTotal_Redemption_xpath).send_keys(TotalRedem)

    def OfferBudget(self, Budget):
        self.driver.find_element(By.NAME, self.txtbudget_name).send_keys(Budget)

    def UserUnlimitedredemCheck(self):
        self.driver.find_element(By.XPATH, self.chbUser_redemption_name).click()

    def MultiRdptionPerReceipt(self):
        self.driver.find_element(By.XPATH, self.radiobtnUsereEligible_Multieredem_perReciept).click()

    def SingleRdptionPerReceipt(self):
        self.driver.find_element(By.XPATH, self.radiobtnUsereEligible_Singleredem_perReciept).click()

    def clickOnStores(self):
        Stores = self.driver.find_element(By.XPATH, self.txtStores_xpath)
        Stores.click()  # Click on the tags input field
        return Stores

    def clickOnCountry(self):
        self.driver.find_element(By.XPATH, self.drpdwnCountry_xpath).click()

    def clickOnCountryselect(self):
        self.driver.find_element(By.XPATH, self.lsSelect_country).click()

    def clickOnGroup(self, Group):
        self.driver.find_element(By.XPATH, txtTargeted_group_xpath).send_keys(Group)


    def clickOnOffer(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpoffer_xpath)).click()
        drp.select_by_visible_text(value)

    def clickOnOfferType(self):
        self.driver.find_element(By.XPATH, self.drpofferType_xpath).click()


    def clickOnCashback(self, Cashback):
        self.driver.find_element(By.XPATH, self.txtCashback_xpath).send_keys(Cashback)

    def clickOnTotalMinQty(self, Value):
        self.driver.find_element(By.XPATH, self.txtTotal_Minqty_xpath).send_keys(Value)

    def clickOnProductName(self, name):
        self.driver.find_element(By.XPATH, self.txtProductName_xpath).send_keys(name)

    def clickOnReceiptLineItem(self,LineItem):
        self.driver.find_element(By.XPATH, self.txtReceipt_LineItem_xpath).send_keys(LineItem)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()






















