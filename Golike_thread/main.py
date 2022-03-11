import pydub
import urllib
import threading
from time import sleep
from selenium import webdriver
import speech_recognition as sr
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


a = int(input("Nhập số lượng chạy: "))
       
def runtest(t):
       print(f"Đang chạy Profile{t+5}")
       sleep(t*5)
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile{t+6}")
       chrome_options.add_argument("--disable-extensions")
       driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
       
       
       driver.set_window_rect(t*700,0,700,900)
       driver.get("https://app.golike.net/jobs")
       kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
       kiem_tien_ngay.click()
       print("\nkiem tien ngay\n")

       def runtest():
              chon_job = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/span/div[1]/div/div/div/div")))
              try:chon_job.click()
              except:
                     try:
                            chon_job = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/span/div/div/div/div/div/div[2]/div[1]/div[1]/span")))
                            chon_job.click()
                     except:driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div > div:nth-child(2) > div:nth-child(3) > span > div > div").click()')
              print("\nchon job\n")

              text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/span")))
              check_text = text.text
              print("\nlay van ban\n")

              sleep(7)
              driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div:nth-child(2) > div > div > a:nth-child(3) > div.col.px-0 > h6.font-bold.font-18").click()')
              driver.switch_to.window(driver.window_handles[1])
              print("\nlam job\n")

              if "THEO" in check_text:
                     
                     try:
                            follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Follow']")))
                            follow.click()
                     except:
                            ba_cham = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-expanded="false"]')))
                            ba_cham.click()
                            follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="menuitem"]')))
                            follow.click()
                            sleep(2)
                     print("\nFollow\n")
              elif "LIKE" in check_text:
                     try:
                            like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                            like.click()
                     except:
                            pass
                     print("\nLike\n")
              driver.close()
              driver.switch_to.window(driver.window_handles[0])
              sleep(7)
              driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div.card.card-job-detail.hand > div > div").click()')
              print("\nhoan thanh\n")

              try:
                     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title=\"recaptcha challenge expires in two minutes\"]")))
                     print("captcha")
                     audio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-audio-button\"]")))
                     audio.click()

                     print("\naudio\n")

                     play = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\":2\"]")))
                     play.click()
                     print("play")

                     #get the mp3 audio file
                     src = driver.find_element(By.ID, "audio-source").get_attribute("src")
                     print("\n[INFO] Audio src: %s\n" %src)
                     #download the mp3 audio file from the source
                     urllib.request.urlretrieve(src, "sample.mp3")
                     sound = pydub.AudioSegment.from_mp3("sample.mp3")
                     sound.export("sample.wav", format="wav")
                     file_audio = sr.AudioFile("sample.wav")
                     rec = sr.Recognizer()
                     with file_audio as source:
                            audio_data = sr.Recognizer().record(source)
                            audio_text = rec.recognize_google(audio_data)
                     print(audio_text)
                     
                     text_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"audio-response\"]")))
                     text_input.send_keys(audio_text.lower())
                     verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-verify-button\"]")))
                     verify.click()
                     driver.switch_to.default_content()
                     sleep(5)
              except:
                     pass
              
              driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
              print("\nxac nhan hoan thanh\n")

              
       for i in range(a):
              try:
                     runtest()
                     print(f"Hoan thanh job {i+1}")
              except:
                     print(f"Loi job {i+1}")
                     try:
                            sleep(20)
                            driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                     except:
                            pass
                     driver.switch_to.window(driver.window_handles[0])
                     driver.get("https://app.golike.net/jobs")
                     kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
                     kiem_tien_ngay.click()
                     print("\nkiem tien ngay\n")
       
       
       
       sleep(1800)
       
so_luong = 1
thread = []
for i in range(so_luong):
       thread += [threading.Thread(target=runtest,args={i},)]
for i in thread:
       i.start()
for i in thread:
       i.join()

print("Kết thúc")