from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

twitter = open("./Twitter.txt", "r")
data_twitter = [i.strip().split("|") for i in twitter.readlines()]
print(data_twitter)

def twitter(n):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir=c:/temp/profile {n}")
    driver = uc.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://twitter.com/i/flow/login")
    # driver.get("https://twitter.com")
    # sleep(1800)

    sleep(5)
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')))
    email.send_keys(data_twitter[n][0])
    next = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')))
    next.click()
    try:
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
        username.send_keys(data_twitter[n][1])
        next = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/span/span')))
        next.click()
    except:
        pass
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
    password.send_keys(data_twitter[n][2])
    login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span')))
    login.click()
    sleep(20)
    driver.refresh()
    sleep(10)

if __name__ == "__main__":
    for n in range(1):
        try:
            twitter(n)
        except:
            print(f"Lỗi tk dòng thứ {n+1}")
    # sleep(18000)
           