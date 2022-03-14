import pydub
import urllib
import threading
from time import sleep
from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


n = int(input("Nhập số lượng chạy: "))
       
def runtest(t):
       a = t+1
       print(f"Đang chạy Profile{a}")
       sleep(t*5)
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument(f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile{a}")
       driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
       action = webdriver.ActionChains(driver)
       
       if t<2:
              driver.set_window_rect(t*700,0,700,900)
       elif t==2:
              driver.set_window_rect(0,300,700,900)
       elif t==3:
              driver.set_window_rect(700,300,700,900)
       sleep(60)
       driver.get("https://app.golike.net/jobs")
       sleep(3)
       kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
       kiem_tien_ngay.click()
       print("\nkiem tien ngay\n")

       def run():
              try:
                     chon_job = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/span/div[1]/div/div/div/div")))
                     chon_job.click()
              except:
                     driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div > div:nth-child(2) > div:nth-child(3) > span > div:nth-child(1) > div > div > div > div").click()')
              print("\nchon job\n")
              sleep(3)

              text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/span")))
              check_text = text.text
              print("\nlay van ban\n")

              sleep(3)
              driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div:nth-child(2) > div > div > a:nth-child(3) > div.col.px-0 > h6.font-bold.font-18").click()')
              driver.switch_to.window(driver.window_handles[1])
              print("\nlam job\n")
              sleep(5)

              if "THEO" in check_text:
                     try:
                            follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Follow']")))
                            follow.click()
                            
                     except:
                            try:
                                   ba_cham = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-expanded="false"]')))
                                   ba_cham.click()
                                   follow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="menuitem"]')))
                                   follow.click()
                            except:pass
                            
                     print("\nFollow\n")
              elif "LIKE" in check_text:
                     try:
                            likes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Like']")))
                            while likes is False:
                                   driver.execute_script('scrollTo(0,700)')
                            likes[0].click()
                            likes[1].click()
                     except:
                            pass
                     print("\nLike\n")
              elif "LOVE" in check_text:
                     try:
                            like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                            action.click_and_hold(like)
                            action.perform()

                            love = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Love']")))
                            love.click()
                     except:
                            pass
                     print("\nLove\n")
              elif "THƯƠNG" in check_text:
                     try:
                            like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
                            action.click_and_hold(like)
                            action.perform()

                            care = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Care']")))
                            care.click()
                     except:
                            pass
                     print("\nCare\n")
              sleep(3)
              driver.close()
              driver.switch_to.window(driver.window_handles[0])
              sleep(7)
              driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div.card.card-job-detail.hand > div > div").click()')
              print("\nhoan thanh\n")
              try:
                     text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="swal2-content"]'))).text
                     print(f"Luong {a} hoan thanh job {text[-2:]}")
                     sleep(3)
                     driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                     print("\nxac nhan hoan thanh\n")
                     sleep(1)
                     driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                     print("\nxac nhan hoan thanh\n")
                     
              except:
                     pass

              try:
                     sleep(2)
                     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title=\"recaptcha challenge expires in two minutes\"]")))
                     audio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-audio-button\"]")))
                     audio.click()
                     print("captcha")

                     print("\naudio\n")

                     play = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\":2\"]")))
                     play.click()
                     print("play")

                     #get the mp3 audio file
                     src = driver.find_element(By.ID, "audio-source").get_attribute("src")
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
                     sleep(3)
                     text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="swal2-content"]'))).text
                     print(f"Luong {a} hoan thanh job {text[-2:]}")
                     
                     driver.execute_script('document.querySelector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()')
                     print("\nxac nhan hoan thanh\n")
              except:
                     pass
              

              
       for i in range(n):
              try:
                     run()
              except:
                     print(f"Loi hoan thanh")
                     
                     try:
                            driver.switch_to.window(driver.window_handles[1])
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                     except:
                            pass
                     driver.get("https://app.golike.net/jobs")
                     sleep(3)
                     kiem_tien_ngay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/span/div[2]/div/div/div[1]/div[2]/div/div")))
                     kiem_tien_ngay.click()
                     print("\nkiem tien ngay\n")
       
       
so_luong = 3
thread = []
for i in range(so_luong):
       thread += [threading.Thread(target=runtest,args={i},)]
for i in thread:
       i.start()
for i in thread:
       i.join()

print("Kết thúc")