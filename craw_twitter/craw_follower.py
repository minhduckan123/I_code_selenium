from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


f = open("craw_data_followers.txt", "w")
http = "https://twitter.com/bts_bighit/followers"
# http = input("Nhap duong link: ")
m = 1000
# m = input("Nhap so luong craw: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile1")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome("D:/Everything_other/chrome_driver/chromedriver.exe", chrome_options=chrome_options)
action = webdriver.ActionChains(driver)

driver.get(http)
    
def craw_followers(i):
    data = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, f"//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/div/div[2]")))
    data_username = data.text 
    driver.execute_script('scrollBy(0,100)')
    f.write(data_username)
    f.write("\n")
    sleep(0.5)
    
for i in range(1,m):
    i = i%66
    if i == 0:
        continue
    while True:
        try:
            craw_followers(i)
            break
        except:
            driver.execute_script('scrollBy(0,-500)')
            # sleep(0.5)
            
# //*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/div[2]
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]/div/div[2]