from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("9052490500")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("sanjana")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.close()