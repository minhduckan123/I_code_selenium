import random
import datetime
import string
from time import sleep
import threading
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def runtest(t):
       sleep(t*3)
       def generate_password(char_num):
              return ''.join(random.choice(string.ascii_letters) for _ in range(char_num)).capitalize()+f"{random.randint(0,9)}"

       def generate_email(char_num):
              return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

       email = generate_email(random.randint(10,12))+"@gmail.com"
       password = generate_password(random.randint(6,10))

       # print(gmail, password)
       start_date = datetime.date(1980, 1, 1)
       end_date = datetime.date(1999, 1, 1)

       time_between_dates = end_date - start_date
       days_between_dates = time_between_dates.days
       random_number_of_days = random.randrange(days_between_dates)
       random_date = start_date + datetime.timedelta(days=random_number_of_days)

       # print(random_date.year)
       print("Dang chay luong", t)
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.lacoste.com/us/")
       
       x = t*500
       y = 10
       driver.set_window_rect(x,y,500,600)

       driver.get("https://www.lacoste.com/us/")


       send_email = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/section[1]/section[1]/section[1]/form/input[1]")))
       send_email.send_keys(email)

       sign_up = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/section[1]/section[1]/section[1]/form/input[2]")))
       sign_up.click()

       choose_MR = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[1]")))
       choose_MS = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[2]")))
       choose_MRS = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[3]")))

       choose_ = random.randint(1,3)
       if choose_ == 1:
              choose_MR.click()
       elif choose_ == 2:
              choose_MS.click()
       else:
              choose_MRS.click()

       first_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-firstname\"]")))
       first_name.send_keys(email[:5])

       last_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-lastname\"]")))
       last_name.send_keys(email[5:10])

       confirm_email = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-emailConfirmation\"]")))
       confirm_email.send_keys(email)

       Privacy_policy = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[8]/div/label")))
       Privacy_policy.click()

       submit = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-confirm\"]")))
       submit.click()

       sleep(15)
       menu = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"main-menu\"]/button")))
       menu.click()

       sleep(5)
       driver.execute_script('document.querySelector("#main-menu > div > div.nav-wrapper.js-nav-wrapper.nav-lvl0-wrapper.is-active > ul > li.nav-lvl0-tab.cell-mt-25.nav-footer-item.menu-separator > a > span").click()')
       sleep(3)

       create_acc = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login-formpage\"]/section/div/div[2]/section/div/div[2]/a")))
       create_acc.click()

       choose_MRs = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[1]/div/label[1]/input")))
       choose_MSs = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[1]/div/label[2]/input")))
       choose_MRSs = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[1]/div/label[3]/input")))

       if choose_ == 1:
              choose_MRs.click()
       elif choose_ == 2:
              choose_MSs.click()
       else:
              choose_MRSs.click()

       first_names = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[3]/div[1]/input")))
       first_names.send_keys(email[:5])

       last_names = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[3]/div[2]/input")))
       last_names.send_keys(email[5:10])

       emails = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-email1\"]")))
       emails.send_keys(email)

       confirm_emails = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[5]/input")))
       confirm_emails.send_keys(email)

       passwords = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-password1\"]")))
       passwords.send_keys(password)

       confirm_passwords = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[7]/input")))
       confirm_passwords.send_keys(password)

       submits = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[2]/button")))
       submits.click()

       driver.get("https://www.lacoste.com/us/account/orders")
       sleep(5)

       driver.get("https://www.lacoste.com/us/account/profile")
       sleep(5)

       edit_profile = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/article/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/span")))
       edit_profile.click()

       date_time = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"edit-form-popin\"]/div[1]/div[3]/div/label")))
       date_time.send_keys(random_date.day, random_date.month, random_date.year)

       submitss = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"edit-form-popin-confirm\"]")))
       submitss.click()
       sleep(13)

       menu.click()

       driver.execute_script('document.querySelector("#main-menu > div > div.nav-wrapper.js-nav-wrapper.nav-lvl0-wrapper.is-active > ul > li.nav-lvl0-tab.cell-mt-25.nav-footer-item.menu-separator > div.padding-mt-4.fs--small.no-desk > a").click()')

       sleep(1800)


so_luong = 4
threads = []
for t in range(so_luong):
       threads += [threading.Thread(target=runtest,args={t},)]
for t in threads:
       t.start()
for t in threads:
       t.join()
print("Ket thuc so luong")

