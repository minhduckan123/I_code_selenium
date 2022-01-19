from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from random import randint, seed


seed(randint(1,100))
def wait(a,b):
    sleep(randint(a,b))

f = open("account.txt", "r")
username, password = f.readline().strip().split()

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()

driver.get("https://twitter.com/")
wait(9,15)

driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div").click()

sign_in = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")))
sign_in.send_keys(username)
wait(1,3)

driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div").click()
wait(5,7)
driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(password)
wait(1,3)
driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
wait(7,12)

print("Đăng nhập thành công!")



