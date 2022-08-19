import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import csv
import time
import os

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div', 40)
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')
    msg_box.send_keys(Keys.ENTER)
    time.sleep(3)
# for not requiring to scan qr code again and again
chrome_options = Options()
chrome_options.add_argument("--user-data-dir-Session")
chrome_options.add_argument("--profile-directory=Default")

PATH = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=chrome_options)

rows=[]
base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
with open("marks.csv",'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
for i in range(0,len(rows)):
    mssg = """-------{}'s Score-------
    Marks in physics:{}
    Marks in chemistry:{}
    Marks in maths:{}
    Marks in biology:{}
    Please ignore for testing purpose""".format(rows[i][1],rows[i][4],rows[i][5],rows[i][6],rows[i][7])
    
    print(rows[i][1])
    url_msg = base_url.format(rows[i][2], mssg)
    send_message(url_msg)






