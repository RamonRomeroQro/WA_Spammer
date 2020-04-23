import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from selenium.webdriver.firefox.options import Options


DELAY = 10
MESSAGE1= "HOLA jkwenkw"


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get("https://web.whatsapp.com/")
# read qr
print('Scan phone ...')
time.sleep(10)
c1 = driver.find_element_by_xpath(
    "//div[@class='_2S1VP copyable-text selectable-text']")
c1.click()
# read dump from google contacts
f = open('google.csv')

for i, line in enumerate(f):
    if i == 0:
        continue
    else:
        from_contact=line.strip().split(',')[0]
        tofind=from_contact.strip("|").split("|")[1]
        c1.send_keys(from_contact)
        time.sleep(1)
        try:
            e = driver.find_element_by_class_name("_2EXPL")
            e.click()
            ms = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            ms.click()

   
            ms.send_keys(MESSAGE1)
            # ms.send_keys(Keys.SHIFT + Keys.ENTER)
            time.sleep(DELAY)
            ms.send_keys(Keys.ENTER)
            print(from_contact)
        except Exception as e:
            print(e, tofind)

        c1.clear()
       