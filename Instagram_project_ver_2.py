from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC


XPATH_MAIL = '//*[@id="loginForm"]/div/div[1]/div/label/input'
XPATH_PASS = '//*[@id="loginForm"]/div/div[2]/div/label/input'
INSTAGRAM_EMAIL = 'shlomo.mica@outlook.co.il'
INSTAGRAM_URL = 'https://www.instagram.com/accounts/login'
INSTAGRAM_PASSWORD = 'z2!8DM9SeTzpjKx'
s = Service("C:\development2\chromedriver.exe")


class Insta_follower:
    def __init__(self, s_new):
        self.driver1 = webdriver.Chrome(service=s_new)

    def login(self):
        self.driver1.get('https://www.instagram.com/accounts/login')
        time.sleep(2)
        a = self.driver1.find_element(By.XPATH, XPATH_MAIL)
        b = self.driver1.find_element(By.XPATH, XPATH_PASS)
        a.send_keys(INSTAGRAM_EMAIL)
        time.sleep(2)
        b.send_keys(INSTAGRAM_PASSWORD)
        LOGIN = self.driver1.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        LOGIN.click()
        time.sleep(8)
        save_info_button = self.driver1.find_element(By.TAG_NAME, 'button')
        time.sleep(3)
        save_info_button.click()
        # TODO TURN ON NOTIFICITION
        time.sleep(2)
        ui.WebDriverWait(self.driver1, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
        self.driver1.maximize_window()
        #self.find_followers()

    def find_followers(self):
        time.sleep(2)
        self.driver1.find_element(By.LINK_TEXT, value='See All').click()
        time.sleep(4)
        #self.follow()

    def follow(self):
        followe_buttons_list = self.driver1.find_elements(By.TAG_NAME, value='button')
        time.sleep(2)
        for i in range(5):
            followe_buttons_list[i].click()
            time.sleep(2)



insta_bot=Insta_follower(s)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
