import selenium
import webbrowser
import time
webbrowser.open('https://10.197.72.90')
time.sleep( 5 )
username = selenium.find_element_by_name("username")
password = selenium.find_element_by_name("password")
username.send_keys("root")
password.send_keys("roZes123")
selenium.find_element("#xwt_widget_uishell_Header_0 > div > div.headerLeft > div.dijitInline.toggleNode.isOpen").click()