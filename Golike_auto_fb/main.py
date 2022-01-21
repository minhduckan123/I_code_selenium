import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import ssl


# remove verify SSL
ssl._create_default_https_context = ssl._create_unverified_context

driver = uc.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()

i_do = int(input())
# i_do = 10
f = open("account.txt", "r")
i = f.readlines()

username_f, password_f = i[0].strip().split()
username, password = i[1].strip().split()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys(username_f)
driver.find_element(By.XPATH, "//*[@id=\"pass\"]").send_keys(password_f, Keys.RETURN)

time.sleep(5)
driver.get('https://app.golike.net/home')

driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys(username)
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(password)
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()

time.sleep(10)
element_check = WebDriverWait(driver, 1800).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
element_check.click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div").click()
time.sleep(10)

while i_do > 0:
    i_do -=1
    try:
        element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/span/div/div")))
        element.click()
    except:
        try:
            element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/span/div/div/div/div/div/div[2]/div[1]/div[2]/span/span")))
            element.click()
        except:
            pass
        
    try:
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[2]/div[1]/div/div/a[2]").click()
        time.sleep(15)
        try:
            driver.switch_to.window(driver.window_handles[1])
            element_likes = driver.find_elements(By.XPATH, "//div[@aria-label='Like']")
            for element in element_follows:
                try:
                    element.click()
                    time.sleep(4)
                except:
                    pass
            element_follows = driver.find_elements(By.XPATH, "//div[@aria-label='Follow']")
            for element in element_likes:
                try:
                    if element == element_likes[2]:
                        break
                    element.click()
                    time.sleep(4)
                except:
                    pass
            driver.close()
        except:
            pass
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[2]/div[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type = 'button'][@class='swal2-confirm swal2-styled']").click()
        print(i_do, "success!")
    except:
        print("error{}!".format(i_do))
