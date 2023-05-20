from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
#import pyautogui


# Get the WhatsApp message to send
message = "Good NIght"
driver_path= r"chromedriver_win32\chromedriver.exe"
driver= Chrome(executable_path=driver_path)


## IN PROGRESS
name="Priyanshu Parth"
message="Helooooooooooo"
driver_path = r"chromedriver_win32\chromedriver_win32.exe" 
service=Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://web.whatsapp.com/')

input('Scan the QR code and press enter to continue...')

# for row in sheet.iter_rows(min_row=2, values_only=True):

search_box = driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')
search_box.clear()
search_box.send_keys(f'{name}')
driver.implicitly_wait(5)
time.sleep(1)


search_box.send_keys(Keys.RETURN)
time.sleep(1)

message_box = driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="10"]')
message_box.send_keys(f'{message}')
driver.implicitly_wait(5)
message_box.send_keys(Keys.RETURN)

# attach_button = driver.find_element_by_xpath('//div[@title="Attach"]')
# attach_button.click()
# time.sleep(1)
# image_input = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
# image_input.send_keys(image_path)
# time.sleep(3)
# send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
# send_button.click()
# time.sleep(1)


print('Messages sent successfully!')
driver.quit()