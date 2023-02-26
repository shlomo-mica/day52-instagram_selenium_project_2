from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\development2\chromedriver.exe")
driver = webdriver.Chrome(service=s)
XPATH_MAIL = '//*[@id="loginForm"]/div/div[1]/div/label/input'
XPATH_PASS = '//*[@id="loginForm"]/div/div[2]/div/label/input'
INSTAGRAM_EMAIL = 'shlomo.mica@outlook.co.il'
INSTAGRAM_URL = 'https://www.instagram.com/accounts/login'  #
INSTAGRAM_PASSWORD = 'z2!8DM9SeTzpjKx'
# TODO 2 OPTION FIND
# driver.get("https://www.instagram.com/explore/people/")
driver.get(INSTAGRAM_URL)

time.sleep(2)
a = driver.find_element(By.XPATH, XPATH_MAIL)
b = driver.find_element(By.XPATH, XPATH_PASS)
a.send_keys(INSTAGRAM_EMAIL)
time.sleep(2)
b.send_keys(INSTAGRAM_PASSWORD)
LOGIN = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
LOGIN.click()
time.sleep(8)
save_info_button = driver.find_element(By.TAG_NAME, 'button')
time.sleep(3)
save_info_button.click()
# TODO TURN ON NOTIFICITION
time.sleep(2)
ui.WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
driver.maximize_window()
time.sleep(2)

see_all_link='href="/explore/people/'
#'https://www.instagram.com/explore/people/'
followers = driver.find_element(By.LINK_TEXT,value='See all' ).click()

#TODO SCROLL
time.sleep(2)
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(0.5)


#
# //*[@id="mount_0_0_4g"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div/div/div/div/div[2]/div[2]/div/div/div/ul/li[3]/div/div/div/div/div[3]/button
# driver.get("https://www.instagram.com/alyssthomp/")
#