from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


baseUrl = "https://10.197.xx.xx"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
driver.get(baseUrl)
try:
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "id-of-new-element"))
)
finally:
username=driver.find_element_by_id("label_username")
password=driver.find_element_by_id("label_password")
username.send_keys("root")
password.send_keys("xxxxxxx")
driver.quit()
