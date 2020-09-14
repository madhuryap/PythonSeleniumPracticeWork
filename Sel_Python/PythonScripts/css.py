from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath

import time

def usingCss():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=actiUrl)
    time.sleep(4)
    pattern = 'input[name^="username"]'
    pattern = 'input[name$="username"]'
    pattern = 'input[name*="username"]'
    webEleRef = driver.find_element_by_css_selector(pattern)
    print("web element ref is ", webEleRef)
    driver.close()

usingCss()