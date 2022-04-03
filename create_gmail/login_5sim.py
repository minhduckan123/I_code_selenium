import pydub
import urllib
import threading
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



if __name__ == "__main__":
        
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(f"--user-data-dir=C:/temp/create_gmail")
        chrome_options.add_argument("--mute-audio")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        action = ActionChains(driver)
        driver.get("https://5sim.net/login")
        sleep(1800)

        try:
                username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
                username.send_keys("nothing")
                password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="password"]')))
                password.send_keys("nothing")
                WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2']")))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
                driver.switch_to.default_content()
                WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title=\"recaptcha challenge expires in two minutes\"]")))
                sleep(3)
                audio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-audio-button\"]")))
                audio.click()
                print("\naudio\n")
                play = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\":2\"]")))
                play.click()
                print("play")
                #get the mp3 audio file
                src = driver.find_element(By.ID, "audio-source").get_attribute("src")
                # print("\n[INFO] Audio src: %s\n" %src)
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
                sleep(3)
                verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"recaptcha-verify-button\"]")))
                verify.click()
        except:
                pass
        
        sleep(3)
        login = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
        login.click()
        print("\nlogin\n")
        
        
        
        # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '')))