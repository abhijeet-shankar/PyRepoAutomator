from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path= r"chromedriver_win32\chromedriver.exe"
driver= Chrome(executable_path=driver_path)


## IN PROGRESS
## IN PROGRESS
usern=input()
password=input()
driver_path = r"chromedriver_win32\chromedriver_win32.exe" 
service=Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
search_input = driver.find_element(By.XPATH, " //input[@class= '_aa4b _add6 _ac4d'] ")
#search_input.clear()
search_input_pass = driver.find_element(By.XPATH,"//input[@aria-label='Password']")
search_input.send_keys(usern)
search_input_pass.send_keys(password)
# time.sleep(5)
login=driver.find_element(By.XPATH,"//button[@class='_acan _acap _acas _aj1-']").click()
time.sleep(30)
chat=driver.find_element(By.XPATH,f"//a[@href='/direct/inbox/?next=%2Fi{usern}%2F']").click()
time.sleep(5)
#savelog        //input[@id='f27b0ac91ec7db']

time.sleep(10)
driver.quit()