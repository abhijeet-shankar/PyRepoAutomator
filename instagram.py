from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path= r"chromedriver_win32\chromedriver.exe"
driver= Chrome(executable_path=driver_path)


## IN PROGRESS