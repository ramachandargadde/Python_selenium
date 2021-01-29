from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
#time.sleep(1000000)
baseurl="www.google.com"
#baseurl1="https://10.104.119.201"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
driver.get(baseurl)
#driver.find_element(By.ID,"details-button").click()
#driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"label_username").send_keys("15j41a0441@gmail.com")
driver.find_element(By.ID,"label_password").send_keys("XXXXXXXXXXX")
driver.find_element(By.ID,"loginPage_LoginButton_label").click()
time.sleep(10)
#delay=3
#dnacurl=baseurl+"/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en&#pageId=dnac_integration_page_id"
#driver.execute_script("window.open('" +dnacurl + "');")
