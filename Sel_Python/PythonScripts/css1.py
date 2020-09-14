from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

filePath=r""

def cssSelMatch():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=filePath)
    time.sleep(4)
    pattern = ""
    pattern = ""
    pattern = ""
    webEleRef = driver.find_element_by_css_selector(pattern)
    print("web element ref",webEleRef)
    driver.close()

cssSelMatch()