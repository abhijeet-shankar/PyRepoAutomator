import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import Chrome
from selenium import webdriver
import pyautogui

usern=input()
password=input()
receiver=input()
message=input()
subject=input()



driver_path = r"chromedriver_win32\chromedriver_win32.exe" 
service=Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://mail.google.com/")
time.sleep(3)

username=driver.find_element(By.XPATH, " //input[@type='email'] ")
username.send_keys(usern)
pyautogui.press('enter')
time.sleep(15)
# next1=driver.find_element(By.XPATH, "//span[@jsname='V67aGc']").click()

password=driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(password)
pyautogui.press('enter')
time.sleep(2)
# next2=driver.find_element(By.XPATH, "//span[@jsname='V67aGc']").click()

time.sleep(20)

#compose  //div[@class ='T-I T-I-KE L3']
# TO: //input[@id =':1io']
# cc //span[@id =':1gn']
#bcc //span[@id =':1gk']
#subj //input[@id =':1bb']
#message  //div[@id =':1a2']
# attachment //div[@id =':1f9']
#send  //div[@id =':1bl']
#send sched  //div[@id =':1bp']

compose= driver.find_element(By.XPATH, " //div[@class ='T-I T-I-KE L3']").click()
time.sleep(2)
to = driver.find_element(By.XPATH, " //input[@id =':1io']")
to.sendkeys(receiver)

# cc= driver.find_element(By.XPATH, " //span[@id =':1gn'] ")
# cc.send_keys()

subject= driver.find_element(By.XPATH, "//input[@id =':1bb']")
subject.send_keys(subject)
time.sleep(3)
send=  driver.find_element(By.XPATH, "//div[@id =':1bl']").click()
time.sleep(5)

driver.quit()


