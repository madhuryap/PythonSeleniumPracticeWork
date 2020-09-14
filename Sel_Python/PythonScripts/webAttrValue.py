from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

def elementAttr():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=actiUrl)
    webRefUsernameTF = driver.find_element_by_id("username")
    attrName = "placeholder"
    attrValue = webRefUsernameTF.get_attribute(attrName)
    print(attrName,"=",attrValue)
    driver.close()
elementAttr()