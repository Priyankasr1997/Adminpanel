from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateOffer:
    def __init__(self, driver):
        self.driver = driver

    # ---------------- LOCATORS ---------------- #

    btnCreateOffer_xpath = "//button[normalize-space()='CREATE OFFER']"
    autoSearch_Clientcompany_xpath = "//input[@placeholder='Client Company']"
    txtTitle_xpath = "//input[@name='title']"
    txtSubtitle_name = "subtitle"
    txtPromotional_xpath = "//textarea[@name='promotionalText']"
    txtTerms_xpath = "//textarea[@name='terms']"
    txtDescription_xpath = "//textarea[@name='description']"

    txtTags_xpath = "//input[@id='tags-standard']"

    txtProduct_Logo_xpath = "//input[@name='logo']"
    txtProduct_Image1_xpath = "//input[@name='images.0.image']"

    txtFromDate_xpath = "(//span[@role='spinbutton' and @aria-label='Year'])[1]"
    txtToDate_xpath = "(//span[@role='spinbutton' and @aria-label='Year'])[2]"

    txtUser_Redemption_xpath = "//input[@name='individualRedemptionLimit']"
    txtTotal_Redemption_xpath = "//input[@name='totalRedemptionLimit']"
    txtbudget_name = "budget"


    unlimitedredemptioncheckbox_perperson_xpath = "(//input[@type='checkbox'])[3]"
    rdobtn_singleredem_perperson = "//input[@value='single']"

    txtStores_xpath = "//input[@placeholder='Stores (Brands)']"

    drpdwnCountry_xpath = "//div[@id='mui-component-select-country']"
    lsSelect_country = "//li[@data-value='FI']"

    drpoffer_xpath = "//div[@id='mui-component-select-cashbackOfferKind']"
    drpofferType_xpath = "//li[@data-value='Volume']"

    txtCashback_xpath = "//input[@name='cashbackValue']"
    txtTotal_Minqty_xpath = "//input[@name='minTotalProductCount']"
    txtProductName_xpath = "//input[@name='products.0.productName']"
    txtReceipt_LineItem_xpath = "//input[@name='products.0.receiptLineItemText.0']"

    btnSave_xpath = "//button[text()='Save']"

    # ---------------- BASIC ACTIONS ---------------- #


    def clickOnCreateOffer(self):
        self.driver.find_element(By.XPATH, self.btnCreateOffer_xpath).click()

    def select_client_company(self, company_name):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.autoSearch_Clientcompany_xpath))
        )
        element.click()
        element.clear()
        element.send_keys(company_name)

        # Wait for dropdown suggestion and click it
        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'test company')]"))
        )
        option.click()

    def clickOnTags(self):
        element = self.driver.find_element(By.XPATH, self.txtTags_xpath)
        element.click()
        return element

    def clickOnProductLogo(self, image_url):
        self.driver.find_element(By.XPATH, self.txtProduct_Logo_xpath).send_keys(image_url)

    def ClickOnImage1(self, image_url):
        self.driver.find_element(By.XPATH, self.txtProduct_Image1_xpath).send_keys(image_url)

    def clickOnFromDate(self, from_date):
        self.driver.find_element(By.XPATH, self.txtFromDate_xpath).send_keys(from_date)

    def clickOnToDate(self, to_date):
        self.driver.find_element(By.XPATH, self.txtToDate_xpath).send_keys(to_date)

    def UserUnlimitedredemCheck(self):
        self.driver.find_element(By.XPATH, self.unlimitedredemptioncheckbox_perperson_xpath).click()

    def SingleRdptionPerReceipt(self):
        self.driver.find_element(By.XPATH, self.rdobtn_singleredem_perperson).click()

    def select_store(self, store_name):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.txtStores_xpath))
        )
        element.click()
        element.send_keys(store_name)

        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'" + store_name + "')]"))
        )
        option.click()

    def clickOnCountry(self):
        self.driver.find_element(By.XPATH, self.drpdwnCountry_xpath).click()

    def clickOnCountryselect(self):
        self.driver.find_element(By.XPATH, self.lsSelect_country).click()

    def clickOnOffer(self):
        self.driver.find_element(By.XPATH, self.drpoffer_xpath).click()

    def clickOnOfferType(self):
        self.driver.find_element(By.XPATH, self.drpofferType_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    # ================= VALIDATIONS ================= #

    def get_success_message(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'MuiSnackbar') or contains(@class,'MuiAlert')]")
                )
            )
            return element.text
        except:
            return ""

    def is_validation_error_present(self):
        errors = self.driver.find_elements(By.XPATH, "//p[contains(@class,'Mui-error')]")
        return len(errors) > 0

    def get_validation_errors(self):
        errors = self.driver.find_elements(By.XPATH, "//p[contains(@class,'Mui-error')]")
        return [e.text for e in errors]

    # =========================================================
    # 🔥 REUSABLE METHODS (NO DUPLICATION)
    # =========================================================

    def fill_basic_details(self, data):
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).send_keys(data["title"])
        self.driver.find_element(By.NAME, self.txtSubtitle_name).send_keys(data["subtitle"])
        self.driver.find_element(By.XPATH, self.txtPromotional_xpath).send_keys(data["promo"])
        self.driver.find_element(By.XPATH, self.txtTerms_xpath).send_keys(data["terms"])
        self.driver.find_element(By.XPATH, self.txtDescription_xpath).send_keys(data["description"])

    def fill_redemption_details(self, data):
        self.driver.find_element(By.XPATH, self.txtUser_Redemption_xpath).send_keys(data["user_redemption"])
        self.driver.find_element(By.XPATH, self.txtTotal_Redemption_xpath).send_keys(data["total_redemption"])
        self.driver.find_element(By.NAME, self.txtbudget_name).send_keys(data["budget"])

    def fill_offer_details(self, data):
        self.driver.find_element(By.XPATH, self.txtCashback_xpath).send_keys(data["cashback"])
        self.driver.find_element(By.XPATH, self.txtTotal_Minqty_xpath).send_keys(data["min_qty"])
        self.driver.find_element(By.XPATH, self.txtProductName_xpath).send_keys(data["product"])
        self.driver.find_element(By.XPATH, self.txtReceipt_LineItem_xpath).send_keys(data["receipt"])