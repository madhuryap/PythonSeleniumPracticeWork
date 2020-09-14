from selenium import webdriver
from selenium.webdriver.common.by import By
from Sel_Python.setting import chromePath
from Sel_Python.setting import actiBaseUrl,fbUrl
driver = webdriver.Chrome(executable_path=chromePath)

def ID_Loc(actiBaseUrl):
    driver.get(actiBaseUrl)
    driver.maximize_window()
    webEleRef1= driver.find_element_by_id("username")
    print("web element ref1", webEleRef1)
    webEleRef=driver.find_element(By.ID,"username")
    print("web element ref",webEleRef)
    driver.close()

def ClassName_loc(fbUrl):
    driver.get(fbUrl)
    driver.maximize_window()
    webEleRef = driver.find_element(By.CLASS_NAME,"textField")
    webEleRef=driver.find_element_by_class_name("textfield")
    print("web element ref", webEleRef)
    driver.close()

ID_Loc(actiBaseUrl)
ClassName_loc(fbUrl)