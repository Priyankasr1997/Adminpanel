import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # browser will not automatically close
Serv = Service(r'C:\Users\Priyanka Ramareddy\PycharmProjects\practice\downloads\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=Serv)
wait = WebDriverWait(driver, 10)
# login
driver.get("https://panelv4-staging.rabble.com/login")

driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

driver.find_element(By.NAME, "email").send_keys("srpriyanka995@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()

#create offer
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='CREATE OFFER']").click()
time.sleep(10)





# Wait until the checkbox is present
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='redemptionPersonCheckbox']")))

# Check if the checkbox is enabled
if checkbox.is_enabled():
    # Check if the checkbox is already selectedc
    if checkbox.is_selected():
        # Wait for the radio button for multiple redemptions per person to be present
        multiple_redem_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='limitation'][1]")))

        # Check if the radio button for multiple redemptions per person is selected
        if multiple_redem_radio.is_selected():
            # Click on the radio button for single redemption per person
            single_redem_radio = driver.find_element(By.XPATH, "/input[@name='limitation'][2]")
            single_redem_radio.click()

