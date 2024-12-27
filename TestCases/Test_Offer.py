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
Serv = Service(r'C:\Users\Priyanka Ramareddy\PycharmProjects\Adminpanel\downloads\chromedriver.exe')
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
time.sleep(5)
element=driver.find_element(By.XPATH, "//input[@placeholder='Client Company']")   ##Client company autosearch dropdown
element.click()
xpath="//input[@placeholder='Client Company']"
time.sleep(6)
#actions = ActionChains(driver)
#driver.find_element(By.XPATH, "//input[@aria-activedescendant='mui-973576768-option-0']")
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys("1756: test company")
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(Keys.RETURN)
wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(Keys.TAB)


Title= driver.find_element(By.ID, "outlined-basic")         ##Title inputfield
Title.send_keys("A T")

SubTitle=driver.find_element(By.NAME, "subtitle")      ##subtitle inputfield
SubTitle.send_keys("Testing")

PromotionalText=driver.find_element(By.XPATH,"(//textarea[@name='textarea'])[1]")   ##promotional text inputfield
PromotionalText.send_keys("Energy Drink")

TermsDescription=driver.find_element(By.XPATH,"(//textarea[@name='textarea'])[2]")   ## Terms inputfield
TermsDescription.send_keys("Testing")

LongDescription=driver.find_element(By.XPATH,"(//textarea[@name='textarea'])[3]") ##description inputfield
LongDescription.send_keys("Testing this Box")


Tags=driver.find_element(By.XPATH,"//input[@id='tags-standard']")   ##tags inputfield
Tags.send_keys("Drinks")
Tags.send_keys(Keys.ENTER)

Logo= driver.find_element(By.XPATH,"//input[@name='logoUrl']")     ##logo inputfield
Logo.send_keys("https://res.cloudinary.com/rabble-staging/image/upload/v1634549905/coke_product_image_uc6jky.png")

Image1= driver.find_element(By.NAME,"images_0")     ##product detail image1 inputfield
Image1.send_keys("https://res.cloudinary.com/rabble-staging/image/upload/v1634549905/coke_product_image_uc6jky.png")

# Time Period

FromDateTime= driver.find_element(By.XPATH,"//input[@placeholder='yyyy-mm-dd hh:mm']")    ##FromDate Calender date picker
FromDateTime.send_keys("2023-06-20 08:04")

ToDateTime= driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd hh:mm'])[2]")  ##ToDate Calender picker
ToDateTime.send_keys("2023-06-30 08:04")


# Until_FurtherNotice=driver.find_element(By.XPATH,"//input[@name='timePeriodCheckbox']").click()  #Until Further Notice Checkbox


#Limitations

PerPerson_Redemptions=driver.find_element(By.XPATH,"//input[@name='redemptionPerson']")
PerPerson_Redemptions.send_keys('1')

Total_Redemptions=driver.find_element(By.XPATH,"//input[@name='redemptionTotal']")
Total_Redemptions.send_keys("1000")

#Multiple Redemptions Per person Check box
# Unlimited_Redemptions= driver.find_element(By.XPATH,"//input[@name='redemptionPersonCheckbox']").click()

#Unlimited redemption in total Check box
# UnlimitedTotalRedemptions= driver.find_element(By.XPATH,"//input[@name='redemptionTotalCheckbox']").click()

#Eligible to multiple redemption per receipt Radio button
# Multiple_Redemption= driver.find_element(By.XPATH,"//input[@value='multiple']").click()

#Eligible to 1 redemption per receipt Radio button
One_Redemption= driver.find_element(By.XPATH,"//input[@value='single']").click()


#Available at

Stores=driver.find_element(By.XPATH,"//input[@placeholder='Stores (Brands)']")   ##autosearch dropdown
Stores.click()
Stores.send_keys('SE')
time.sleep(10)
# 2nd Store Entry
Stores.send_keys(Keys.ENTER)
Stores.send_keys('Or')
time.sleep(7)
Stores.send_keys(Keys.ENTER)

Country=driver.find_element(By.XPATH,"(//div[@id='standard-select-currency'])[1]")  ##dropdown
Country.click()
time.sleep(5)
Select=driver.find_element(By.XPATH,"//li[@data-value='SE']").click()  #SE,FI,NO,DK


#Offer Mechanism

Offer= driver.find_element(By.XPATH,"(//div[@id='standard-select-currency'])[2]").click()     ##offer type
OfferType= driver.find_element(By.XPATH,"//li[@data-value='Single']").click() # Single,Volume,Bundle

#Manual Review Checkbox
# ManualReview= driver.find_element(By.XPATH,"//input[@name='verifyManualCheckbox']").click()

Cashback=driver.find_element(By.XPATH,"(//div[@id='standard-select-currency'])[3]").click()
SelectCashback=driver.find_element(By.XPATH,"//li[@data-value='Percentage']").click() # Fixed,Percentage

CashbackValue=driver.find_element(By.XPATH,"//input[@name='offerMechanismCashback']")   ##cashbackvalue
CashbackValue.send_keys(Keys.BACKSPACE)
CashbackValue.send_keys("10")

MaxCashback=driver.find_element(By.XPATH,"//input[@name='offerMechanismMaxCashback']")   ##max cahsbackvalue
MaxCashback.send_keys(Keys.BACKSPACE)
MaxCashback.send_keys('1')

#Products

MinQuantity=driver.find_element(By.XPATH,"//input[@name='minProductQuantity']")
MinQuantity.send_keys(Keys.BACKSPACE)
MinQuantity.send_keys('1')

#Always verify Physical products (force barcode scanning) Checkbox
#VerifyPhysical=driver.find_element(By.XPATH,"//input[@name='verifyPhysicalCheckbox']").click()

ProductName=driver.find_element(By.XPATH,"//input[@name='productName_0']")    ##product name
ProductName.send_keys("TestData")

#EANNumber=driver.find_element(By.XPATH,"//input[@name='barCode_0']").send_keys("12345678")

#SelectEANType=driver.find_element(By.XPATH,"//div[@id='mui-component-select-barCodeType_0']").click()
#EANType=driver.find_element(By.XPATH,"//li[@data-value='EAN 8']").click() #EAN 8, EAN 13


Receipt_ItemText=driver.find_element(By.XPATH,"(//input[@type='text'])[16]")
Receipt_ItemText.send_keys("Rio")
time.sleep(5)
Save=driver.find_element(By.XPATH,"//button[normalize-space()='SAVE']").click()
#AddReceiptText=driver.find_element(By.XPATH,"//button[normalize-space()='Receipt Text']").click()
#AddReceiptText.send_keys("hello")

# Receipt_ItemText2=driver.find_element(By.XPATH,"(//input[@type='text'])[18]")
# Receipt_ItemText2.send_keys("TestData2")

# DeleteIcon=driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M6 19c0 1.')]").click()
