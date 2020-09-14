import time
from Sel_Python.setting import chromePath,actiUrl
from selenium import webdriver
driver = webdriver.Chrome(chromePath)
driver.get(actiUrl)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_css_selector("a#loginButton").click()
time.sleep(4)
res= driver.get_cookies()
driver.close()

driver = webdriver.Chrome(chromePath)
driver.get(actiUrl)
for i in res:
    driver.add_cookie(i)

driver.refresh()
time.sleep(4)
print("app closed")
#driver.quit()