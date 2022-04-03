from random import randint
from time import sleep
from datetime import datetime
import os
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


name_ = "Hoàng"
wallet = open("./Wallet.txt", "r")
data_wallet = [i.strip() for i in wallet.readlines()]

twitter = open("./Twitter.txt", "r")
data_twitter = [i.strip().split("|") for i in twitter.readlines()]


m = range(46)

def celebrate(n):
    file_ = open("request.txt", "a", encoding="utf-8")
    file_.write(f"Tài khoản thứ {n+1}:\n")
    os.system("rasdial /disconnect")
    os.system("rasdial mobi")
    # sleep(5)
    global driver
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir=c:/temp/profile {n}")
    # chrome_options.headless = True
    driver = uc.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://gleam.io/FrcBf/to-celebrate-our-partners-we-are-giving-away-50000-angl?gsr=FrcBf-NVtlgWoCwE&fbclid=IwAR3iZm8VL_8nmB_BpPZhBFllt3U6rTKo8QJspwR_Pfz2LnOZtqRp4UrqBis")
    sleep(5)
    driver.execute_script('scrollBy(0,10000)')

    try:
        visit_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/a/span[1]/span')))
        visit_more.click()
        print("\nvisit ... more\n")
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/div/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input')))
        name.send_keys(name_)
        print("\nname\n")
        mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/div/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input')))
        mail.send_keys(data_twitter[n][0])
        icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/div/div/form/fieldset[2]/div[3]/div[1]/div/label/span[1]')))
        icon.click()
        sleep(2)
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/div/div/form/div/span[1]/button/span[2]')))
        save.click()
        print("\nsave\n")
        try:
            click_twitter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="other-logins"]/div[1]/div/ul/li[1]/a')))
            click_twitter.click()
            print("\ntwitter\n")
        except:
            pass
        driver.execute_script('document.querySelector("#em6274816 > div > div > form > div.form-compact__content > div > p:nth-child(2) > a").click()')
        print("\nclick here\n")
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274816"]/div/div/form/div[2]/div/a/span[2]')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 1.\n")
    except:
        file_.write(f"Nhiệm vụ số 1 đã hoàn thành từ trước.\n")
        pass
    
    try:
        answer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274819"]/a/span[1]/span/span')))
        answer.click()
        print("\nanswer\n")
        i = randint(1,5)
        img_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="em6274819"]/div/div/form/div/div[1]/ul/li[{i}]/a')))
        img_.click()
        print(f"img {i}")
        sleep(3)
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274819"]/div/div/form/div/div[2]/button')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 2.\n")
    except:
        file_.write(f"Nhiệm vụ số 2 đã hoàn thành từ trước.\n")
        pass
    
    try:
        visit_reddit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274820"]/a/span[1]/span/span')))
        visit_reddit.click()
        print("\nvisit ... reddit\n")
        visit_reddit_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274820"]/div/div/form/div[1]/div[2]/a')))
        visit_reddit_1.click()
        print("\nvisit ... reddit\n")
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274820"]/div/div/form/div[2]/div/a[1]')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 3.\n")
    except:
        file_.write(f"Nhiệm vụ số 3 đã hoàn thành từ trước.\n")
        pass
    sleep(5)
    
    try:
        subscribe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274817"]/a/span[1]/span/span')))
        subscribe.click()
        print("\nsubscribe\n")
        subscribe_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274817"]/div/div/form/div[1]/div[1]/p/a')))
        subscribe_now.click()
        print("\nsubscribe now\n")
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274817Details"]')))
        text.send_keys(subscribe_now.get_attribute("href"))
        print("\ntext\n")
        sleep(3)
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274817"]/div/div/form/div[2]/div/a/span[2]')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 4.\n")
    except:
        file_.write(f"Nhiệm vụ số 4 đã hoàn thành từ trước.\n")
        pass
    
    try:
        view_instagram = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274818"]/a/span[1]/span/span')))
        view_instagram.click()
        print("\nview instagram\n")
        sleep(6)
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274818"]/div/div/form/div[2]/div/a')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 5.\n")
    except:
        file_.write(f"Nhiệm vụ số 5 đã hoàn thành từ trước.\n")
        pass
    
    try:
        answer_question = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274822"]/a/span[1]/span/span')))
        answer_question.click()
        print("\nrefer .. entries\n")
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274822Details"]')))
        text.send_keys(data_wallet[n])
        print("\ntext\n")
        sleep(3)
        continue_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274822"]/div/div/form/div[2]/div/a/span[2]')))
        continue_.click()
        print("\ncontinue\n")
        file_.write(f"Hoàn thành nhiệm vụ số 7.\n")
    except:
        file_.write(f"Nhiệm vụ số 7 đã hoàn thành từ trước.\n")
        pass
    try:
        bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6274821"]/a/span[1]')))
        bar.click()
        print("\nbar\n")
    except:
        print(f"\n{n}error6\n")
        
        pass
    file_.write('-'*20+'\n')
    sleep(5)
    file_.close()
    driver.close()
    
if __name__ == "__main__":
    for n in m:
        celebrate(n)   
    f_ = open("request.txt", "a", encoding="utf-8")
    f_.write("Đã kết thúc vào lúc:\n")
    f_.write(f"{datetime.now()}\n")   
    f_.write(f"="*40+"\n")  
    f_.close()