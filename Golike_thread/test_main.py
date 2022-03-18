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
    chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile6")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("https://app.golike.net/jobs/facebook?load_job=true")
    try:
            sleep(3)
            theo_doi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/span")))
            theo_doi.click()
            print("theo doi")
    except: pass
    
    sleep(1800)