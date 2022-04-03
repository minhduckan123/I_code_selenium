from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


f = open("craw_data_quotes.txt", "w")
http = "https://twitter.com/bts_bighit/status/1505484319313182720/retweets/with_comments"
href = "https://twitter.com/search?f=live&vertical=default&q=url:1505484319313182720"
# http = input("Nhap duong link: ")
m = 1000
# m = input("Nhap so luong craw: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile1")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window()

driver.get(href)
a=[]
sleep(10)
for j in range(3):
    print(f"\n{j}\n")
    try:
        for i in range(1,100):
            data = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, f"//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[{i}]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]")))
            a.append(data.text.split("\n")[1])
            
    except:
        pass
    a = list(set(a))
    driver.execute_script('scrollBy(0,100000)')
f.write("\n".join(a))
f.close()
n = input("Nhan Enter de dung...")
