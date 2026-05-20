from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Duplicateoffer:
    # Locators
    MenuIndex = "//button[@aria-controls='simple-menu']"
    btnCreateduplicate = "//li[text()='Create Duplicate']"
    txtFromDate_xpath = "//input[@placeholder='yyyy-mm-dd hh:mm']"
    txtToDate_xpath = "(//input[@placeholder='yyyy-mm-dd hh:mm'])[2]"
    btnSave_xpath = "//button[text()='Save']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 sec wait for elements

    def clickOnListMenu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MenuIndex))).click()

    def clickOnCreateDuplicate(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnCreateduplicate))).click()

    def clickOnFromDate(self, FromDate):
        from_date_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.txtFromDate_xpath)))
        from_date_input.clear()
        from_date_input.send_keys(FromDate)

    def clickOnToDate(self, ToDate):
        to_date_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.txtToDate_xpath)))
        to_date_input.clear()
        to_date_input.send_keys(ToDate)

    def clickOnSave(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnSave_xpath))).click()
