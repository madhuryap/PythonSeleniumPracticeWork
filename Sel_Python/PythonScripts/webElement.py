from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath

def elementTagname():
    driver=webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=actiUrl)
    webEleRef = driver.find_element_by_id("username")
    #webEleRef1= driver.find_element_by_link_text("Forgot your password?")
    #webEleRef2 = driver.find_element_by_partial_link_text("Forgot your")
    result = webEleRef.tag_name
    print("The tag name is ", result)
    #print("Text of the link is", webEleRef1.text)
    #print("The tag name is", webEleRef2.tag_name)
    driver.close()

elementTagname()
