from pydoc import describe
import random, string
import datetime
import threading
from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == "__main__":
    
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=C:/temp/Profile7")
    chrome_options.add_argument('--proxy-server=socks5://52.187.145.233:1080')
    chrome_options.add_argument("--mute-audio")
    driver = uc.Chrome(options= chrome_options)
    driver.maximize_window()
    
    driver.get("https://checkip.com.vn/")
    sleep(1800)