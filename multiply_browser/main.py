import random
import string
from time import sleep
import pyautogui
import threading
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

f = open("acc.txt", "r")
email_list = [i.split(":")[0] for i in f.readlines()]

so_luong = 4


def runtest(t):
       sleep(t*10)


       # print(random_date.year)
       print("Dang chay luong", t)
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.lacoste.com/us/")
       
       x = t*500
       if t<4:
              driver.set_window_rect(x,0,500,600)
       elif t<8:
              x= (t-4)*500
              driver.set_window_rect(x,600,500,600)

       # driver.maximize_window()


       for i in range(0,26):
              driver.delete_all_cookies()
              sleep(5)
              driver.get("https://www.lacoste.com/us/")
              try:
                     email = email_list[i*4+t]
                     send_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/section[1]/section[1]/section[1]/form/input[1]")))
                     send_email.send_keys(email)
                     print("\nsend email\n")

                     sign_up = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/section[1]/section[1]/section[1]/form/input[2]")))
                     sign_up.click()
                     print("\nsign up\n")

                     choose_MR = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[1]")))
                     choose_MS = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[2]")))
                     choose_MRS = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[1]/div/label[3]")))
                     print("\nchoose\n")

                     choose_ = random.randint(1,3)
                     if choose_ == 1:
                            choose_MR.click()
                     elif choose_ == 2:
                            choose_MS.click()
                     else:
                            choose_MRS.click()

                     first_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-firstname\"]")))
                     first_name.send_keys(email[:3])
                     print("\nfirst name\n")

                     last_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-lastname\"]")))
                     last_name.send_keys("thuy")
                     print("\nlast name\n")

                     email_ = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-email\"]")))
                     email_.clear()
                     sleep(3)
                     email_.send_keys(email)
                     print("\nemail\n")

                     confirm_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-emailConfirmation\"]")))
                     confirm_email.send_keys(email)
                     print("\nconfirm email\n")

                     Privacy_policy = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-form\"]/div[8]/div/label")))
                     Privacy_policy.click()
                     print("\nprivacy policy\n")

                     submit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"newsletter-confirm\"]")))
                     submit.click()
                     print("\nsubmit\n")

                     sleep(20)
                     menu = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"main-menu\"]/button")))
                     menu.click()
                     print("\nmenu\n")

                     sleep(5)
                     driver.execute_script('document.querySelector("#main-menu > div > div.nav-wrapper.js-nav-wrapper.nav-lvl0-wrapper.is-active > ul > li.nav-lvl0-tab.cell-mt-25.nav-footer-item.menu-separator > a > span").click()')
                     print("\nSome thing\n")
                     sleep(3)
                     
                     email_create = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-email\"]")))
                     email_create.send_keys(email)
                     print("\nemail create\n")
                     
                     continue_ = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-continue\"]")))
                     continue_.click()
                     print("\ncontinue\n")
                     
                     create_my_acc = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-signup\"]")))
                     create_my_acc.click()
                     print("\ncreate my acc\n")
                     
                     create_password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-password\"]")))
                     create_password.send_keys("Thuy97@")
                     print("\ncreate password\n")
                     password_confirm = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-passwordConfirmation\"]")))
                     password_confirm.send_keys("Thuy97@")
                     print("\nconfirm password\n")

                     choose_MRs = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin-signup-form\"]/div/div[4]/div/label[1]")))
                     choose_MSs = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin-signup-form\"]/div/div[4]/div/label[2]")))
                     choose_MRSs = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin-signup-form\"]/div/div[4]/div/label[3]")))
                     print("\nchoose\n")

                     if choose_ == 1:
                            choose_MRs.click()
                     elif choose_ == 2:
                            choose_MSs.click()
                     else:
                            choose_MRSs.click()
                     
                     first_names = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-firstName\"]")))
                     first_names.send_keys(email[:3])
                     print("\nfirst name\n")

                     last_names = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-lastName\"]")))
                     last_names.send_keys("thuy")
                     print("\nlast name\n")
                     
                     # date_time = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin-signup-form\"]/div/div[8]/div/label")))
                     # date_time.click()
                     # pyautogui.write(date_of_birth, 0.001)
                     # print("\ndate time\n")
                     
                     check_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin-signup-form\"]/div/div[10]/div/label")))
                     check_box.click()
                     print("\ncheck box\n")
                     
                     validate = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"signin_signup-register\"]")))
                     validate.click()
                     print("validate")
                     sleep(4)
                     print(f"\nThanh cong luong{t} tk{i} dong {i*4+t+1}\n")
              except:
                     print(f"\nloi luong{t} tk {i} dong {i*4+t+1}\n")
       


threads = []
for t in range(so_luong):
       threads += [threading.Thread(target=runtest,args={t},)]
for t in threads:
       t.start()
for t in threads:
       t.join()
print("Ket thuc so luong")

