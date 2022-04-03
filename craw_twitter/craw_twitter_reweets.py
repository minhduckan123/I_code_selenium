from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


f = open("craw_data_reweets.txt", "w")
http = "https://twitter.com/bts_bighit/status/1505831662671650817/retweets"
# http = input("Nhap duong link: ")
m = 100
# m = input("Nhap so luong craw: ")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile6")
driver = webdriver.Chrome("D:/Everything_other/chrome_driver/chromedriver.exe", chrome_options=chrome_options)
action = webdriver.ActionChains(driver)

driver.get(http)
sleep(10)

a = []
for j in range(800):
    print(f"\n{j}\n")
    try:
        for i in range(1,100):
            data = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span")))
            a.append(data.text)
    except:
        pass
    a = list(set(a))
    driver.execute_script('document.querySelector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div").scrollBy(0,100000)')

f.write("\n".join(a))
f.close()
