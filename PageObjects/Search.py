import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # browser will not automatically close

###listing all the elements
class Search:
    searchbtn_id = "input-search-header"
    clearBtn_xpath = type= "(//button[@type='button'])[4]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchoffer(self):
        search = self.driver.find_element(By.ID, self.searchbtn_id)
        search.click()
        return search
        time.sleep(3)





