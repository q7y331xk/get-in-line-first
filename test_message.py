from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pyperclip

def set_chrome_driver(silence):
    chrome_options = webdriver.ChromeOptions()
    if silence:
        chrome_options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def google_msg(silence):
    driver = set_chrome_driver(silence)
    driver.get("https://messages.google.com/web/authentication")
    sleep(20)
    cookies = driver.get_cookies()
    return { 'driver': driver, 'cookies': cookies}

def set_cookies(cookies):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    session = requests.Session()
    session.headers.update(headers)
    for cookie in cookies:
        c = {cookie['name']: cookie['value']}
        session.cookies.update(c)
    return session

pairing = google_msg(False)
cookies = pairing["cookies"]
driver = pairing["driver"]
html = driver.page_source
html_parsed = BeautifulSoup(html, "html.parser")
print(html_parsed)
link = driver.find_element(By.CSS_SELECTOR,'a.mat-focus-indicator').click()
sleep(2)
pyperclip.copy("010-9971-2502")
driver.find_element(By.CSS_SELECTOR,'input.input').click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
sleep(1)



