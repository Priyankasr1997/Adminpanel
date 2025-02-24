import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)  # browser will not automatically close

class CreateOffer:
    #adding all the locatores for the create offer page
    btnCreateOffer_xpath = "//button[normalize-space()='CREATE OFFER']"      #"//*[@id='root']/div[6]/main/div/div[1]/div/div/div/div[2]/button"
    autoSearch_Clientcompany_xpath = "//input[@placeholder='Client Company']"
    time.sleep(3)
    txtTitle_xpath = "//input[@name='title']"
    txtSubtitle_name = "subtitle"
    txtPromotional_xpath = "//textarea[@name='promotionalText']"
    txtTerms_xpath = "//textarea[@name='terms']"
    txtDescription_xpath = "//textarea[@name='description']"
    txtTags_xpath = "//input[@id='tags-standard']"
    txtProduct_Logo_xpath = "//input[@name='logo']"
    txtProduct_Image1_xpath = "//input[@name='images.0.image']"
    txtFromDate_xpath = "//input[@placeholder='yyyy-mm-dd hh:mm']"
    txtToDate_xpath = "(//input[@placeholder='yyyy-mm-dd hh:mm'])[2]"
    txtUser_Redemption_xpath = "//input[@name='individualRedemptionLimit']"
    txtTotal_Redemption_xpath = "//input[@name='totalRedemptionLimit']"
    unlimitedredemptioncheckbox_perperson_xpath = "(//input[@type='checkbox'])[3]" ###User unlimited redemption per person
    rdobtn_multipleredem_perperson = "//input[@value='multiple']"    ##multile redemption per person radio button
    unlimit_total_redem = "(//input[@type='checkbox'])[4]"    ####total unlimited redemption checkbox
    Hidetotalredemptio_xpath ="(//input[@type='checkbox'])[5]"
    rdobtn_singleredem_perperson = "//input[@value='single']" ###single redemption per persion
    txtbudget_name = "budget"
    #radiobtnUsereEligible_Multieredem_perReciept = "//input[@name='limitation']"
    #radiobtnUsereEligible_Singleredem_perReciept = "(//input[@name='limitation'])[2]"
    txtStores_xpath = "//input[@placeholder='Stores (Brands)']"
    drpdwnCountry_xpath = "//div[@id='mui-component-select-country']"
    lsSelect_country = "//li[@data-value='FI']"
    txtTargeted_group_xpath = "//input[@placeholder='Group']"
    drpoffer_xpath = "//div[@id='mui-component-select-cashbackOfferKind']" ##select dropdown
    drpofferType_xpath = "//li[@data-value='Volume']"   #select offer tyepe  ---//li[@data-value='Bundle']
    txtCashback_xpath = "//input[@name='cashbackValue']"
    txtTotal_Minqty_xpath = "//input[@name='minTotalProductCount']"
    txtProductName_xpath = "//input[@name='products.0.productName']"
    txtReceipt_LineItem_xpath = "//input[@name='products.0.receiptLineItemText.0']"
    btnSave_xpath = "///button[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCreateOffer(self):
        self.driver.find_element(By.XPATH, self.btnCreateOffer_xpath).click()

    def clickClientCompany(self):
        self.driver.find_element(By.XPATH, self.autoSearch_Clientcompany_xpath).click()

    def clickTitle(self, Title):
        edit_title = self.driver.find_element(By.XPATH, self.txtTitle_xpath)
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
        self.driver.find_element(By.XPATH, self.txtProduct_Image1_xpath).send_keys(Image1)

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
        self.driver.find_element(By.XPATH, self.unlimitedredemptioncheckbox_perperson_xpath).click()

    def MultiRdptionPerReceipt(self):
        self.driver.find_element(By.XPATH, self.rdobtn_multipleredem_perperson).click()

    def SingleRdptionPerReceipt(self):
        self.driver.find_element(By.XPATH, self.rdobtn_singleredem_perperson).click()

    def clickOnStores(self):
        Stores = self.driver.find_element(By.XPATH, self.txtStores_xpath)
        Stores.click()  # Click on the tags input field
        return Stores


    def clickOnCountry(self):
        self.driver.find_element(By.XPATH, self.drpdwnCountry_xpath).click()

    def clickOnCountryselect(self):
        self.driver.find_element(By.XPATH, self.lsSelect_country).click()

    def clickOnGroup(self, Group):
        self.driver.find_element(By.XPATH, self.txtTargeted_group_xpath).send_keys(Group)


    def clickOnOffer(self):
        self.driver.find_element(By.XPATH, self.drpoffer_xpath).click()
        #drp.select_by_visible_text(value)

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






















