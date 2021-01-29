from selenium import webdriver
from selenium.webdriver.common.by import By

def my_function(url):
    driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
    driver.get("https://"+url)
    driver.find_element(By.ID,"details-button").click()
    driver.find_element(By.ID,"proceed-link").click()
    driver.find_element(By.ID,"label_username").send_keys("root")
    driver.find_element(By.ID,"label_password").send_keys("Public123")
    driver.find_element(By.ID,"loginPage_LoginButton_label").click()
    #driver.get("https://"+url+"/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en#pageId=LicenseCenter_pageId&queryParams=command%3DwcsFiles%26subMenuBitMask%3D1_LicenseFiles&forceLoad=true")
    return 0
url="10.104.119.209"
my_function(url)



from selenium import webdriver
from selenium.webdriver.common.by import By
url="10.104.119.209"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
driver.get("https://"+url)
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"label_username").send_keys("root")
driver.find_element(By.ID,"label_password").send_keys("Public123")
driver.find_element(By.ID,"loginPage_LoginButton_label").click()
#driver.get("https://"+url+"/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en#pageId=LicenseCenter_pageId&queryParams=command%3DwcsFiles%26subMenuBitMask%3D1_LicenseFiles&forceLoad=true")


