import random, string
import datetime
import threading
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



if __name__ == "__main__":
        m = int(input("Nhập số lượng gmail cần tạo: "))
        last_name = ["Nam", "Duy", "Huy", "Tuan", "Kien", "Nhi", "Thi", "Thu",
                "Ly", "Anh", "Nga", "Duc", "Manh", "Duy", "Tien",
                "Dung", "Hung", "Quang", "Tien", "Ngoc", "Chuong", 
                "Bach", "Khanh", "Huong", "Chi", "Linh", "Quan", "Nhan",
                "Ngoc", "Yen", "Khanh", "Hieu", "Bich"]
        first_name = ["Dinh", "Tran", "Tong", "Do", "Le", "Quach",
                        "Trinh", "Bui", "Nguyen", "Pham", "Phan", "Lai"] 
        f = open("gmail.txt", "a", encoding="utf-8")
        f.write("-"*20 +f"\nThời gian tạo: {datetime.datetime.now()}\n" )

        #Nhập password vào đây
        password = "stronger312"
        
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(f"--user-data-dir=C:/temp/create_gmail")
        chrome_options.add_argument("--mute-audio")
        driver = uc.Chrome(options= chrome_options)
        driver.maximize_window()
        action = ActionChains(driver)
        def create_gmail():
                email_list = []
                for x in range(1):
                        email_list.append(random.choice(last_name))
                        email_list.append(random.choice(first_name))
                for x in range(random.randint(5,6)):
                        email_list.append(random.choice(string.digits))
                gmail = "".join(email_list)
                
                print(gmail)
                
                driver.get('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail%26oq%3Dgm%26aqs%3Dchrome.1.69i57j0i131i433i512l2j0i131i433j0i131i433i512l3j0i131i433j0i433i512.1388j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&hl=vi&dsh=S-2063496369%3A1648658428510164&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
                last_name_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="lastName"]')))
                last_name_text.send_keys(email_list[0])
                first_name_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="firstName"]')))
                first_name_text.send_keys(email_list[1])
                username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="Username"]')))
                username.send_keys(gmail)
                password_01 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="Passwd"]')))
                password_01.send_keys(password)
                confirm_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="ConfirmPasswd"]')))
                confirm_password.send_keys(password, Keys.RETURN)
                sleep(5)
                driver.execute_script('''window.open("https://5sim.net/");''')
                sleep(5)
                driver.switch_to.window(driver.window_handles[1])
                vietnam = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="btn-group btn-matrix"]/button[171]')))
                vietnam.click()
                sleep(3)    
                google_01 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody/tr[104]/td[2]')))
                google_01.click()
                buy = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody/tr[104]/td[3]/button')))
                buy.click()
                sleep(5)
                copy_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Copy with prefix"]')))
                copy_number.click()
                driver.switch_to.window(driver.window_handles[0])
                paste_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="phoneNumberId"]')))
                paste_number.send_keys(Keys.CONTROL + "v", Keys.RETURN)
                while True:
                        try:
                                sleep(5)
                                note = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div')))
                                print(note.text)
                                number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="phoneNumberId"]')))
                                number.clear()
                                driver.switch_to.window(driver.window_handles[1])
                                cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[2]/td/a[1]/button')))
                                cancel.click()
                                sleep(4)
                                buy_again = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[3]/td/a[2]/button')))
                                buy_again.click()
                                sleep(3)
                                copy_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Copy with prefix"]')))
                                copy_number.click()
                                driver.switch_to.window(driver.window_handles[0])
                                paste_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="phoneNumberId"]')))
                                paste_number.send_keys(Keys.CONTROL + "v", Keys.RETURN)
                        except:
                                break
                driver.switch_to.window(driver.window_handles[1])
                try:
                        buy_again = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[3]/td/a[2]/button')))
                        buy_again.click()
                        print("Đã hết số. Xin dừng chương trình!")
                        raise Exception("Đã hết số. Đã dừng chương trình!")
                except:
                        pass
                while True:
                        try:
                                copy_code = WebDriverWait(driver, 480).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr[7]/td[2]/div/div/button')))
                                copy_code.click()
                                break
                        except:
                                print("Không nhận được mã!")
                                cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[2]/td/a[1]/button')))
                                cancel.click() 
                                sleep(4)
                                buy_again = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[3]/td/a[2]/button')))
                                buy_again.click()
                driver.switch_to.window(driver.window_handles[0])
                sleep(1)
                paste_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="code"]')))
                paste_code.send_keys(Keys.CONTROL + "v", Keys.RETURN)
                sleep(4)
                day = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="day"]')))
                f.write(gmail + "|stronger312\n")
                f.close()
                day.send_keys("23")
                element = driver.find_element(By.XPATH, '//select[@id="month"]')
                all_months = element.find_elements(By.TAG_NAME, "option")
                month = random.randint(2,11)
                all_months[month].click()
                year = random.randint(1970,2000)
                year_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="year"]')))
                year_text.send_keys(f'{year}')
                element_gender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//select[@id="gender"]')))
                all_gender = element_gender.find_elements(By.TAG_NAME, "option")
                gender = random.randint(1,2)
                all_gender[gender].click()
                recovery_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="recoveryEmail"]')))
                recovery_email.send_keys(Keys.RETURN)
                sleep(2)
                dong_y_01 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')))
                dong_y_01.click()
                sleep(2)
                dong_y_02 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
                dong_y_02.click()
                driver.switch_to.window(driver.window_handles[1])
                finish = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tfoot/tr[4]/td/a/button')))
                finish.click()
                sleep(3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                # sleep(1800)
                
                # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))
                # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))
                # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))
                # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))
                # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))
        for i in range(m):
                create_gmail()