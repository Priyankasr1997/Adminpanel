from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    textbox_username_name ="email"
    textbox_password_name ="paswword"
    button_login_xpath = "//button[normalize-space()='Sign in']"

    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_name = "email"
        self.textbox_password_name = "password"
        #self.button_login_xpath ="//button[normalize-space()='Sign in']"

    def setUserName(self, username):
        #self.driver.find_element_by_id(self.textbox_username_name).clear()
        #self.driver.find_element(By.NAME.textbox_username_name).send_keys(username)
        username_input = self.driver.find_element(By.NAME, self.textbox_username_name)
        username_input.send_keys(username)

    def setPassword(self, password):
        #self.driver.find_element_by_id(self.textbox_password_id).clear()
        #self.driver.find_element(By.NAME.textbox_password_name).send_keys(password)
        username_input = self.driver.find_element(By.NAME, self.textbox_password_name)
        username_input.send_keys(password)

    #def ClickLogin(self):
     #   self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def ClickLogin(self):
        #login_button = self.driver.find_element_by_xpath(self.button_login_xpath)
        #login_button.click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()



