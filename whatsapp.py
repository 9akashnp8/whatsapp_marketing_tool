import os
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

url = "https://web.whatsapp.com/"

#Open chrome and go to webwhatsapp and wait until scanned
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

#list of numbers to send messages to
#list_of_numbers = ["7907251041", "7907317290", "8848334496", "9249373320", "9656169933"]
df = pd.read_excel("E:\Private\Programming\VSCode\SDFC\Book1.xlsx")

#Message to send
message = "Testing"

#Main Loop
for i in range(len(df)):
    recipient_number = df.loc[i, "Numbers"]
    send_url = f"https://web.whatsapp.com/send?phone=91{recipient_number}"
    driver.get(send_url)

    #From the webpage, find and click on the "compose" button
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[2]/div'))).click()

    #Variabalize the search text field and enter the number from list of numbers
    number_search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    number_search.send_keys(message)


    #Click on the result (assuming only one)
    #time.sleep(2)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]'))).click()

    #Variabalize the message text field and enter the message
    #message_text_field = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    #message_text_field.send_keys(message)

    #Click on the send button
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
    time.sleep(2)


