import pydub
import urllib
from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile1")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("https://app.golike.net/jobs/facebook?load_job=true")

    sleep(1800)