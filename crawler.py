from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading, time


# Threads  
thread_list = []


# Return page with url
def get_page(url: str) -> object:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    return browser


# Listen for New Content in Hackerone.com (!! Only new programs section !!)
def hackerone_listen_content():
    url = "https://hackerone.com/directory/programs?order_direction=DESC&order_field=launched_at"
    page_content = get_page(url)
    time.sleep(10)
    print(page_content)

hackerone_listen_content();

