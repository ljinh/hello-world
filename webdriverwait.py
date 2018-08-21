from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
locator = (By.ID,"kw")
 
try:
    ele = WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
    driver.find_element_by_id("kw").send_keys('abc')
    time.sleep(1) #为了看效果
except:
    print("ele can't find")
finally:
    driver.quit()
