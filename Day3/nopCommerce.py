from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()
