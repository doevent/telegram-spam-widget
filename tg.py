# -*- coding: utf8 -*-

# python version 3.7.7
# pip install selenium
# download https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

import time
import random

import datetime
import logging

log_filename = f'telegram-{datetime.datetime.now().strftime("%d-%m-%y")}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, filemode='w', format=' %(asctime)s: %(name)s - %(levelname)s - %(message)s')


options = webdriver.ChromeOptions()
options.add_argument('--lang=en')
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

# mask head
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
    """
    })

driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})


driver.set_window_rect(10,10, 550, 550)
driver.get("https://oauth.telegram.org/auth?bot_id=111111111&origin=http%3A%2F%2Fsimle.website&embed=1&request_access=write")


def telephone(num, a, b): # slow number
    for tel in num:
        ActionChains(driver).send_keys(tel).perform()
        time.sleep(random.randrange(a, b))
        
driver.implicitly_wait(10) # seconds

with open(f"phone120.txt", "r", encoding="utf-8") as f:
    ph = f.readlines()
    all_phone_num = len(ph)
    count = 0
    for phone_num in ph:
        
        txt = list(phone_num[1:].replace('\n',''))

        telephone(txt, 1, 2) # send slow number

        time.sleep(random.randrange(1, 3))
        ActionChains(driver).send_keys(Keys.RETURN).perform() # send enter key
        ActionChains(driver).reset_actions()
        time.sleep(random.randrange(5, 10))
        driver.delete_all_cookies()
        time.sleep(random.randrange(1, 3))
        driver.refresh()
        time.sleep(random.randrange(5, 10))
        count = count + 1
        phone_w = phone_num.replace('\n','')
        print (f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> {phone_w} -> {count} of {all_phone_num}")



driver.close()