from random import randint
import pydub
import os
import urllib
import threading
from time import sleep
import pyautogui
import undetected_chromedriver.v2 as uc
import speech_recognition as sr
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

if __name__ == "__main__":
       ua = UserAgent()
       userAgent = ua.random
       path = "C:/Users/Lenovo T460/Pictures/Screenshots"
       # n = input("Nhập số lượng chạy: ")
       count_job = {}
       n = "97"      
       text_ = "0"
       so_luong = range(2)
       thread = []

       def wait(a):
              sleep(a)
              
       def runtest(t):
              a = t+3
              count_job[f"{a}"] = "0"
              print(f"Đang chạy Profile{a}")
              wait(t*10)
              chrome_options = uc.ChromeOptions()
              chrome_options.add_argument(f"--user-data-dir=C:/temp/Profile{a}")
              chrome_options.add_argument("--proxy-server= socks5:")
              chrome_options.add_argument("--mute-audio")
              # chrome_options.add_argument(f"user-agent={userAgent}")
              driver = uc.Chrome(options=chrome_options)
              action = ActionChains(driver)
              # sleep(1800)
              if t<3:
                     driver.set_window_rect(t*600,0,600,700)
              elif t==3:
                     driver.set_window_rect(0,700,600,700)
              elif t==4:
                     driver.set_window_rect(600,700,600,700)
              wait(50)
              driver.get("https://app.golike.net/jobs")
              
              # sleep(18000)
              wait(2)
              kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
              kiem_tien_ngay.click()
              print(f"\nLuong {a} kiem tien ngay\n")
              wait(1)
              def run():
                     global text_
                     wait(1)
                     driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div > div:nth-child(2) > div:nth-child(3) > span > div:nth-child(1) > div > div").click()')
                     print(f"\nLuong {a} chon job\n")
                     texts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/span")))
                     check_text = texts.text
                     print(f"\nLuong {a} lay van ban\n")

                     if "THEO" in check_text:
                            mbasic = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[3]")))
                            mbasic.click() 
                            wait(1)
                            driver.switch_to.window(driver.window_handles[1])
                            print(f"\nLuong {a} lam job\n")
                            try:
                                   follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/a")))
                                   follow.click()
                            except: pass
                            print(f"\nLuong {a} Follow\n")
                     elif "LIKE" in check_text:
                            trinh_duyet = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[2]')))
                            trinh_duyet.click()
                            print(f"\nLuong {a} lam job\n")
                            wait(1)
                            driver.switch_to.window(driver.window_handles[1])
                            try:
                                   likes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Like']")))
                                   if "FANPAGE" in check_text:
                                          likes[0].click()
                                   else:
                                          likes[0].click()
                                          likes[1].click()
                            except:
                                   pass
                            print(f"\nLuong {a} Like\n")
                     elif "LOVE" in check_text:
                            trinh_duyet = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[2]')))
                            trinh_duyet.click()
                            wait(1)
                            driver.switch_to.window(driver.window_handles[1])
                            print(f"\nLuong {a} lam job\n")
                            try:
                                   like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                                   action.click_and_hold(like)
                                   action.perform()

                                   love = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Love']")))
                                   love.click()
                            except:
                                   pass
                            print(f"\nLuong {a} Love\n")
                     elif "THƯƠNG" in check_text:
                            trinh_duyet = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[2]')))
                            trinh_duyet.click()
                            wait(1)
                            driver.switch_to.window(driver.window_handles[1])
                            print(f"\nLuong {a} lam job\n")
                            try:
                                   like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                                   action.click_and_hold(like)
                                   action.perform()

                                   care = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Care']")))
                                   care.click()
                            except:
                                   pass
                            print(f"\nLuong {a} Care\n")
                     wait(2)
                     driver.close()
                     driver.switch_to.window(driver.window_handles[0])
                     hoan_thanh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/h6[2]')))
                     hoan_thanh.click()
                     print(f"\nLuong {a} hoan thanh\n")
                     try:
                            text = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="swal2-content"]'))).text
                            count_job[f"{a}"] = text[-2:]
                            print(f"Luong {a} hoan thanh job {count_job[f'{a}']}/{n}")
                            driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                            print(f"\nLuong {a} xac nhan hoan thanh\n")
                     except:
                            pass

                     try:
                            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title=\"recaptcha challenge expires in two minutes\"]")))
                            audio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-audio-button\"]")))
                            audio.click()
                            print(f"Luong {a} captcha")
                            print(f"\nLuong {a} naudio\n")
                            wait(1)
                            play = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\":2\"]")))
                            play.click()
                            print(f"Luong {a} play")
                            #get the mp3 audio file
                            src = driver.find_element(By.ID, "audio-source").get_attribute("src")
                            #download the mp3 audio file from the source
                            urllib.request.urlretrieve(src, f"sample{a}.mp3")
                            sound = pydub.AudioSegment.from_mp3(f"sample{a}.mp3")
                            sound.export(f"sample{a}.wav", format="wav")
                            file_audio = sr.AudioFile(f"sample{a}.wav")
                            rec = sr.Recognizer()
                            with file_audio as source:
                                   audio_data = sr.Recognizer().record(source)
                                   audio_text = rec.recognize_google(audio_data)
                            print(audio_text)
                            text_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"audio-response\"]")))
                            text_input.send_keys(audio_text.lower())
                            wait(1)
                            verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-verify-button\"]")))
                            verify.click()
                            driver.switch_to.default_content()
                            text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="swal2-content"]'))).text
                            count_job[f"{a}"] = text[-2:]
                            print(f"Luong {a} hoan thanh job {count_job[f'{a}']}/{n}")
                            driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                            print(f"\nLuong {a} xac nhan hoan thanh\n")
                     except:
                            pass
              while count_job[f"{a}"] != n:
                     try:
                            run()
                            driver.refresh()
                     except:
                            print(f"Thu lai luong {a} ")
                            try:
                                   driver.switch_to.window(driver.window_handles[1])
                                   driver.close()
                                   driver.switch_to.window(driver.window_handles[0])
                            except:
                                   pass
                            driver.get("https://app.golike.net/jobs")
                            wait(1)
                            kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
                            kiem_tien_ngay.click()
                            print(f"\nkiem tien ngay\n")
                            wait(10)
              driver.close()
                            
       for i in (so_luong):
              thread += [threading.Thread(target=runtest,args={i},)]
       for i in thread:
              i.start()
       for i in thread:
              i.join()

       print("Kết thúc")
       # Turn off window
       # os.system("shutdown /s ")