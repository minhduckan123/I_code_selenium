from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


a = int(input("Nhập số lượng chạy: "))
       
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window()

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
              like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']")))
              like.click()
              print("\nLike\n")
       driver.close()
       driver.switch_to.window(driver.window_handles[0])
       sleep(7)
       driver.execute_script('document.querySelector("#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div.card.card-job-detail.hand > div > div").click()')
       print("\nhoan thanh\n")
       sleep(7)
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
              


#  send_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/section[1]/section[1]/section[1]/form/input[1]")))