import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import ssl
from time import sleep
from random import randint, seed


seed(randint(1,100))
def wait(a,b):
    sleep(randint(a,b))

# remove verify SSL
ssl._create_default_https_context = ssl._create_unverified_context

f = open("account.txt", "r")
username, password, emailuser = f.readline().split()

driver = uc.Chrome()
# driver = webdriver.Chrome("Path to chromedriver")
driver.maximize_window()

driver.get("https://twitter.com/")
wait(8,13)
driver.execute_script("window.scrollBy(0, 100)")
wait(2,4)
driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div").click()
wait(2,4)

sign_in = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")))
sign_in.send_keys(username)
wait(3,5)
driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div").click()
wait(5,7)
try:
    driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(emailuser)
    wait(2,4)
    driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div").click()
    wait(3,4)
except:
    pass
driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(password)
wait(3,5)
driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()

print("Đăng nhập thành công!")

# Thoi gian su dung
wait(1800, 1801)
