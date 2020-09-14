from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

def elementAttr():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=actiUrl)
    webRefUsernameTF = driver.find_element_by_id("username")
    attrName = "placeholder"      # if given attribute is not present it returns none
    attrValue = webRefUsernameTF.get_attribute(attrName)
    print(attrName,"=",attrValue)
    #result = webRefUsernameTF.location  #returns {'x': 644, 'y' : 294}
    #result = webRefUsernameTF.size  #returns {'height':32, 'width': 214}
    #result = webRefUsernameTF.rect  #returns {'height': 32, 'width':214, 'x':644, 'y':294}
    #print(result["x"],type(result))
    #print(result.get("y"))
    #res = webRefUsernameTF.value_of_css_property("padding-leftggg")
    #print((res))
    driver.close()
elementAttr()