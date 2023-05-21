from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

usern=input()
password=input()
frndname=input()
message=input()


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


chat=driver.get('https://www.instagram.com/direct/inbox/')
#chat=driver.find_element(By.XPATH,f"//a[@href='/direct/inbox/?next=%2Fi{usern}%2F']").click()
time.sleep(10)

#savelog        //input[@id='f27b0ac91ec7db']

# new message //div[@class='_abm0']
newmessage=driver.find_element(By.XPATH,"//div[@class='x78zum5 x6s0dn4 xl56j7k xdt5ytf']").click()
time.sleep(2)

#search //div[@class='_aa2t']
search=driver.find_element(By.XPATH,"//input[@name='queryBox']")
search.send_keys(frndname)
time.sleep(2)


# tick 1st search //div[@class='_abm0']
searchclick=driver.find_element(By.XPATH,"//div[@aria-label='Toggle selection']").click()
time.sleep(2)



#button next //button[@class='_acan _acao _acas _acav _aj1-']
next=driver.find_element(By.XPATH,"//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x9bdzbf x1n2onr6 x1d5wrs8 xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq']").click()
time.sleep(2)


# textarea //textarea[@placeholder='Message...']
mes_send=driver.find_element(By.XPATH,"//div[@aria-describedby='Message']")
mes_send.send_keys(message)
time.sleep(2)



#send message //div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1emribx x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']
final=driver.find_element(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1emribx x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']").click()
time.sleep(2)



time.sleep(10)
driver.quit()