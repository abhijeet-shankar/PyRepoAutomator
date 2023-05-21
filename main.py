from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def github_repo_create(usern,password,projname,desc,n):
    driver_path = r"chromedriver_win32\chromedriver_win32.exe" 
    service=Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://github.com/login")
    search_input = driver.find_element(By.ID, "login_field")
    search_input.clear()
    search_input.send_keys(usern)
    search_input = driver.find_element(By.ID, "password")
    search_input.clear()

    search_input.send_keys(password)
    search_input.send_keys(Keys.RETURN)
    time.sleep(15)

    driver.get('https://github.com/new')

    search_input = driver.find_element(By.ID, "react-aria-2")
    search_input.clear()
    search_input.send_keys(projname)
    time.sleep(2)
    if (desc):
        search_input = driver.find_element(By.ID, "react-aria-3")
        search_input.clear()
        search_input.send_keys(desc)
        time.sleep(2)
    else:
        pass    

    if n=='Public':
        search_input = driver.find_element(By.ID, "react-aria-5")
        search_input.click()
    else:
        search_input = driver.find_element(By.ID, "react-aria-6")
        search_input.click()

    time.sleep(2)

    search_input= driver.find_element(By.CSS_SELECTOR,".fAcoGo")
    search_input.click()
    time.sleep(10)
    driver.quit()
