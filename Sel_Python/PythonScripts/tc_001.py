chromePath=r"C:\Users\WORK\PycharmProjects\PythonSelenium\Sel_Python\drivers\chromedriver.exe"

from selenium import webdriver
driver = webdriver.Chrome(executable_path=chromePath)
#webdriver.Chrome(chromePath)

appUrl = "https://www.gmail.com"
actiTimeUrl="https://demo.actitime.com/login.do"
'''
def TC_0001():
    appUrl="https://www.gmail.com"
    driver.get(url=appUrl)
    print("app Url",appUrl,"entered")
    #driver.close()
    driver.quit()
    print("chrome closed")
    #driver.get(appUrl)

def TC_0002():
    driver = webdriver.Chrome(executable_path=chromePath)
    appUrl = "https://www.gmail.com"
    driver.get(url=appUrl)
    AppTitle= driver.title
    if "gmail"== AppTitle.lower():
        print("Enter the username and pwd")
    else:
        print("Not a valid page")
        driver.close()

    print("App title name is :",AppTitle)


TC_0001()
TC_0002()

def Curr_url():
    driver = webdriver.Chrome(executable_path=chromePath)
    appUrl = "https://www.gmail.com"
    actiTimeUrl="https://demo.actitime.com/login.do"
    driver.get(url=appUrl)
    url1=driver.current_url
    print("first url is ",url1)
    driver.get(url=actiTimeUrl)
    url2=driver.current_url
    print("url2 is", url2)
    if url1 != actiTimeUrl:
        print("In actitime page")
    else:
        print("Its not actitime app")

Curr_url()

def pageCode():
    driver = webdriver.Chrome(chromePath)
    driver.get(actiTimeUrl)
    driver.maximize_window()
    driver.minimize_window()
    code= driver.page_source
    print("page source is \n",code)
    import json as j
    c_code=j.dumps(code)
    fileObj=open("actitimePage.text","w")
    fileObj.write(c_code)
    fileObj.close()

pageCode()

def BackMethod():
    driver = webdriver.Chrome(chromePath)
    driver.get(actiTimeUrl)
    url1=driver.current_url
    driver.get(appUrl)
    url2=driver.current_url
    print("url1",url1,"url2",url2)
    driver.back()
    currentUrl=driver.current_url
    if url1==currentUrl:
        driver.refresh()
        print("Page refreshed")
        driver.forward()
        currentUrl=driver.current_url
        print(currentUrl,"after refresh")

BackMethod()
'''
import time

def setSize():
    driver=webdriver.Chrome(chromePath)
    driver.get(actiTimeUrl)
    driver.maximize_window()
    driver.set_window_size(800,900)
    time.sleep(6)
    driver.set_window_position(450,350)
    time.sleep(6)
    driver.set_window_rect(450,300,500,400)
    time.sleep(6)
    print("Window size checked")
    winSize=driver.get_window_size() #used to return h & w of the window
    winPos = driver.get_window_position()
    winRect = driver.get_window_rect()
    print("window size", winSize, "win pos is",winPos, "win rect",winRect)
    driver.close()

setSize()
