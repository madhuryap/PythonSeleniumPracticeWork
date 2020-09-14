from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

def enterAndClick():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=actiUrl)
    time.sleep(4)
    #welEleRef = driver.find_element_by_id("username")
    #welEleRef.send_keys("admin")
    #print(welEleRef)
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("manager")
    print("username and pwd entered")
    time.sleep(4)
    driver.find_element_by_css_selector("a#loginButton").click()
    time.sleep(4)
    driver.close()

enterAndClick()