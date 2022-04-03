from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


f = open("craw_data_quotes.txt", "w")
http = "https://twitter.com/bts_bighit/status/1505484319313182720/retweets/with_comments"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile1")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
action = webdriver.ActionChains(driver)

driver.get(http)

sleep(1800)