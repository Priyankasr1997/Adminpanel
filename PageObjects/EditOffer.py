import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OfferEdit:
    ##Listing all the needful locators to edit te offer
    lsOffer_xpath = "//tbody//tr[1]//td[2]"   #to select 2 record          ###"//p[normalize-space()='ID: 589']"
    btnEditoffer_xpath = '//button[.="EDIT OFFER"]'
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
    unlimitedredemptioncheckbox_perperson_xpath = "(//input[@type='checkbox'])[3]"  ###User unlimited redemption per person
    rdobtn_multipleredem_perperson = "//input[@value='multiple']"  ##multile redemption per person radio button
    unlimit_total_redem = "(//input[@type='checkbox'])[4]"  ####total unlimited redemption checkbox
    Hidetotalredemptio_xpath = "(//input[@type='checkbox'])[5]"
    rdobtn_singleredem_perperson = "//input[@value='single']"  ###single redemption per persion
    txtbudget_name = "budget"
    # radiobtnUsereEligible_Multieredem_perReciept = "//input[@name='limitation']"
    # radiobtnUsereEligible_Singleredem_perReciept = "(//input[@name='limitation'])[2]"
    txtStores_xpath = "//input[@placeholder='Stores (Brands)']"
    drpdwnCountry_xpath = "//div[@id='mui-component-select-country']"
    lsSelect_country = "//li[@data-value='FI']"
    txtTargeted_group_xpath = "//input[@placeholder='Group']"
    drpoffer_xpath = "//div[@id='mui-component-select-cashbackOfferKind']"  ##select dropdown
    drpofferType_xpath = "//li[@data-value='Volume']"  # select offer tyepe  ---//li[@data-value='Bundle']
    txtCashback_xpath = "//input[@name='cashbackValue']"
    txtTotal_Minqty_xpath = "//input[@name='minTotalProductCount']"
    txtProductName_xpath = "//input[@name='products.0.productName']"
    txtReceipt_LineItem_xpath = "//input[@name='products.0.receiptLineItemText.0']"
    btnSave_xpath = "//button[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnListOffer(self):
        self.driver.find_element(By.XPATH, self.lsOffer_xpath).click()

    def clickOnEditOffer(self):
        self.driver.find_element(By.XPATH, self.btnEditoffer_xpath).click()


    def clickClientCompany(self):
        self.driver.find_element(By.XPATH, self.autoSearch_Clientcompany_xpath).click()

    def clickTitle(self, Title):
        title_element = self.driver.find_element(By.XPATH, self.txtTitle_xpath)
        title_element.send_keys(Keys.CONTROL + "a")
        title_element.send_keys(Keys.DELETE)
        title_element.send_keys(Title)
        title_element.click()
        return title_element


    def clickSubTitle(self, Subtitle):
        subtitle_element = self.driver.find_element(By.NAME, self.txtSubtitle_name)
        subtitle_element.send_keys(Keys.CONTROL + "a")
        subtitle_element.send_keys(Keys.DELETE)
        subtitle_element.send_keys(Subtitle)
        subtitle_element.click()
        return subtitle_element

    def clickOnPromotionalText(self, Promotional):
        promo_text = self.driver.find_element(By.XPATH, self.txtPromotional_xpath)
        promo_text.send_keys(Keys.CONTROL + "a")
        promo_text.send_keys(Keys.DELETE)
        promo_text.send_keys(Promotional)
        promo_text.click()
        return promo_text


    def clickOnTerms(self, Terms):
        Terms_text=self.driver.find_element(By.XPATH, self.txtTerms_xpath)
        Terms_text.send_keys(Keys.CONTROL + "a")
        Terms_text.send_keys(Keys.DELETE)
        Terms_text.send_keys(Terms)
        Terms_text.click()
        return Terms_text

    def clickOnDescription(self, Description):
        Des_text = self.driver.find_element(By.XPATH, self.txtDescription_xpath)
        Des_text.send_keys(Keys.CONTROL + "a")
        Des_text.send_keys(Keys.DELETE)
        Des_text.send_keys(Description)
        Des_text.click()
        return Des_text

    # def clickOnTags(self):
    #   self.driver.find_element(By.XPATH, self.txtTags_xpath).click()
    def clickOnTags(self,Tags):
        tags = self.driver.find_element(By.XPATH, self.txtTags_xpath)
        tags.send_keys(Keys.CONTROL + "a")
        tags.send_keys(Keys.DELETE)
        tags.send_keys(Tags)
        tags.click()
        return tags

    def clickOnProductLogo(self, Image):
        Logo = self.driver.find_element(By.XPATH, self.txtProduct_Logo_xpath)
        Logo.send_keys(Keys.CONTROL + "a")
        Logo.send_keys(Keys.DELETE)
        Logo.send_keys(Image)
        Logo.click()
        return Logo

    def ClickOnImage1(self, Image1):
        Image = self.driver.find_element(By.NAME, self.txtProduct_Image1_xpath)
        Image.send_keys(Keys.CONTROL + "a")
        Image.send_keys(Keys.DELETE)
        Image.send_keys(Image1)
        Image.click()
        return Image

    def clickOnFromDate(self, FromDate):
        Fromdate = self.driver.find_element(By.XPATH, self.txtFromDate_xpath)
        Fromdate.send_keys(Keys.CONTROL + "a")
        Fromdate.send_keys(Keys.DELETE)
        Fromdate.send_keys(FromDate)
        Fromdate.click()

    def clickOnToDate(self, ToDate):
        Todate = self.driver.find_element(By.XPATH, self.txtToDate_xpath)
        Todate.send_keys(Keys.CONTROL + "a")
        Todate.send_keys(Keys.DELETE)
        Todate.send_keys(ToDate)
        Todate.click()

    def clickOnUseredemption(self, UserRedem):
        Userred = self.driver.find_element(By.XPATH, self.txtUser_Redemption_xpath)
        Userred.send_keys(Keys.CONTROL + "a")
        Userred.send_keys(Keys.DELETE)
        Userred.send_keys(UserRedem)
        Userred.click()

    def clickOnTotalredem(self, TotalRedem):
        totalred = self.driver.find_element(By.XPATH, self.txtTotal_Redemption_xpath)
        totalred.click()
        totalred.send_keys(Keys.CONTROL + "a")
        totalred.send_keys(Keys.DELETE)
        totalred.send_keys(TotalRedem)


    def OfferBudget(self, Budget):
        budget = self.driver.find_element(By.NAME, self.txtbudget_name)
        budget.click()
        budget.send_keys(Keys.CONTROL + "a")
        budget.send_keys(Keys.DELETE)
        budget.send_keys(Budget)

    def UnlimitedUserredemCheck(self):
        self.driver.find_element(By.NAME, self.unlimitedredemptioncheckbox_perperson_xpath).click()

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

    def clickOnOffer(self):
        self.driver.find_element(By.XPATH, self.drpoffer_xpath).click()

    def clickOnOfferType(self):
        self.driver.find_element(By.XPATH, self.drpofferType_xpath).click()


    def clickOnCashback(self, Cashback):
        amount = self.driver.find_element(By.XPATH, self.txtProductName_xpath)
        amount.send_keys(Keys.CONTROL + "a")
        amount.send_keys(Keys.DELETE)
        amount.send_keys(Cashback)
        amount.click()
        return amount

    def clickOnTotalMinQty(self, Value):
        self.driver.find_element(By.XPATH, self.txtTotal_Minqty_xpath).send_keys(Value)

    def clickOnProductName(self, name):
        product = self.driver.find_element(By.XPATH, self.txtProductName_xpath)
        product.send_keys(Keys.CONTROL + "a")
        product.send_keys(Keys.DELETE)
        product.send_keys(name)
        product.click()
        return product

    def clickOnReceiptLineItem(self, LineItem):
        lineitem = self.driver.find_element(By.XPATH, self.txtReceipt_LineItem_xpath)
        lineitem.send_keys(Keys.CONTROL + "a")
        lineitem.send_keys(Keys.DELETE)
        lineitem.send_keys(LineItem)
        lineitem.click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()




