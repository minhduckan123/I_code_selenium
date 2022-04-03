import pydub
import urllib
import pyautogui
import requests
from time import sleep
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent


ip = "47.242.122.184"
host = "1080"
proxy = {
    "http" : "http://"+"{}:{}".format(ip, host),
    "https" : "https://"+"{}:{}".format(ip, host)
}

path = "D:/Everything_other/chrome_driver/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile7")
ua = UserAgent()
userAgent = ua.random
# chrome_options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(path, options=chrome_options)
driver.maximize_window()
# action = ActionChains(driver)
requests.get("http://",proxies=proxy)
driver.get("https://www.facebook.com")
driver.add_cookie('fr=08LPWTOCUuh2Y8l3U.AWU6a0_lmJVC-RqC8dc1fYjL8Hg.BiNDS4.xI.AAA.0.0.BiQJ_N.AWXFemCm_hU;wd=150x180;m_pixel_ratio=1;datr=uDQ0YhJaTvSIh5Qs6SU2vdps;xs=14:m5AF3YboVyOA:2:1647588536:-1:-1;c_user=100079488519092;sb=9XU0Yv_AosuDK4vbHp_APFIe;')
driver.refresh()
# sleep(8)
# ba_cham = driver.find_element(By.XPATH, '//div[@aria-haspopup="menu"]')
# action.click(ba_cham)
# action.perform()

# follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="menuitem"]')))
# follow.click()
# print("\nfollow\n")
sleep(1800)
