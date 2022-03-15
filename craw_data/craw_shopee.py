import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


f = open("./craw_shopee.csv", "w", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["name", "price 1","price 2", "address", "vote", "sold"])


chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile6")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://shopee.vn/")
sleep(5)
driver.execute_script('document.querySelector("#main > div > div._193wCc._3cVWns > div.home-page > div.container > div.section-below-the-fold > div.section-category-list > div > div > div.shopee-header-section__content > div > div.image-carousel__item-list-wrapper > ul > li:nth-child(9) > div > a:nth-child(1)").click()')
sleep(5)
driver.execute_script("scrollTo(0,2000)")
driver.execute_script('document.querySelector("#main > div > div._193wCc > div > div.container._2AGlcb > div._1-gCzV > div > div.shopee-sort-bar > div.shopee-sort-by-options > div:nth-child(3)").click()')
sleep(5)
driver.execute_script("scrollTo(0,2000)")
sleep(5)
def craw(n):
    for i in range(1,n+1):
        print(i)
        print()
        sleep(3)
        if i < 16:
            driver.execute_script("scrollTo(0,2000)")
        elif i < 31:
            driver.execute_script("scrollTo(0,3000)")
        elif i < 46:
            driver.execute_script("scrollTo(0,4000)")
        elif i < 61:
            driver.execute_script("scrollTo(0,5000)")
        try:
            name = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[{i}]/a/div/div/div[2]/div[1]/div[1]/div')))
            print(name.text)
        except:
            continue
        name_obiject = name.text
        price1 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[{i}]/a/div/div/div[2]/div[2]/div[1]')))
        print(price1.text)
        price_1 = price1.text
        try:
            price2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[{i}]/a/div/div/div[2]/div[2]/div[2]')))
            print(price2.text)
            price_2 = price2.text
        except:price_2 = ""
        address = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[{i}]/a/div/div/div[2]/div[4]')))
        print(address.text)
        address_object = address.text
        try:
            driver.execute_script('document.querySelector("html > div").shadowRoot.querySelector("#troywell-caa > div > div.slider > div.slider__footer > div.btns > div.later").click()')
        except:pass
        name.click()
        sleep(5)
        vote = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]')))
        print(vote.text)
        vote_object = vote.text
        sold  = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[3]/div[1]')))
        print(sold.text)
        sold_object = sold.text
        driver.execute_script('window.history.go(-1)')
        print()
        writer.writerow([name_obiject,price_1,price_2,address_object,vote_object,sold_object])

craw(60)
page2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[3]/div/button[3]')))
page2.click()
sleep(5)
craw(40)
print("\nHoan thanh\n")