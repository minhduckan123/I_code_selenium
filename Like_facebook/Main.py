from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chromium.options import ChromiumOptions
from time import sleep


count_likes = 0
f = open("./account.txt", "r")
username, password = f.read().split()

# options = ChromiumOptions()
# options.headless = True
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element(By.ID, "email").send_keys(username)
driver.find_element(By.ID, "pass").send_keys(password, Keys.RETURN)

sleep(10)

# -------------------------------------------------------------------------------
SCROLL_PAUSE_TIME = 0.1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
# -------------------------------------------------------------------------------

    sleep(10)
    elements = driver.find_elements(
        By.XPATH, ".//div[@class='tvfksri0 ozuftl9m']/div/div[1]/div[@aria-label='Thích'][@role='button']")

    for element in elements:
        try:
            element.click()
            count_likes += 1
            print(f"{count_likes:2} likes")

        except:
            pass
    if count_likes >= 40:
        break
    
driver.close()
