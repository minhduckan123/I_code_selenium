from tkinter import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


#--------------------------------------------------------
# Bác sửa 2 dòng này cho đúng với máy bác nhé
path_to_chromedriver = "D:/Everything_other/chrome_driver/chromedriver.exe"
profile = f"--user-data-dir=C:/Users/Lenovo T460/AppData/Local/Google/Chrome/User Data/Profile1"
#---------------------------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(profile)

def print_hello():
    a=[]
    driver = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
    driver.maximize_window()
    sleep(5)
    id_ = id.get()
    if variable.get() == "craw reweets":
        f = open("craw_data_reweets.txt", "w")
        driver.get(f"https://twitter.com/bts_bighit/status/{id_}/retweets")
        for j in range(int(acc_count.get())//10):
            try:
                for i in range(1,100):
                    data = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span")))
                    a.append(data.text)
            except:
                pass
            a = list(set(a))
            driver.execute_script('document.querySelector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div").scrollBy(0,100000)')
        f.write("\n".join(a))
        f.close()
    elif variable.get() == "craw quotes":
        f = open("craw_data_quotes.txt", "w")
        driver.get(f"https://twitter.com/search?f=live&vertical=default&q=url:{id_}")
        for j in range(int(acc_count.get())//7):
            try:
                for i in range(1,100):
                    data = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, f"//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[{i}]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]")))
                    a.append(data.text.split("\n")[1])
            except:
                pass
            a = list(set(a))
            driver.execute_script('scrollBy(0,100000)')
        f.write("\n".join(a))
        f.close()
  
root = Tk()
root.geometry( "800x400")

label_id = Label(root, text="Enter id status:")
label_id.pack()
id = Entry(root, width=20)
id.pack()

label_acc_count = Label(root, text="Craw number of accounts: ")
label_acc_count.pack()
acc_count = Entry(root, width=10)
acc_count.pack()
  
options = [
    "craw reweets",
    "craw quotes"
]
variable = StringVar(root)
variable.set(options[0])
drop_menu = OptionMenu(root, variable, *options)
drop_menu.pack()
   
button = Button(root, text="Run", command=print_hello, width=15,height=5)
button.pack()

root.mainloop()