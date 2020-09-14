from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

def enterAndClick():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url="https://www.google.com")
    time.sleep(4)
    driver.find_element_by_name("q").send_keys("python")
    time.sleep(3)
    #webEleRef = driver.find_element_by_css_selector("ul[role='listbox']li")
    #print(webEleRef)
    #print(type(webEleRef),"---",len(webEleRef))
    driver.close()

enterAndClick()