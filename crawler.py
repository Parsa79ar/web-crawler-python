from bs4 import BeautifulSoup
import threading
import requests


# Return page with url
def get_page(url: str) -> object:
    page = requests.get(url)
    return page

print(get_page("https://hackerone.com/directory/programs?order_direction=DESC&order_field=launched_at"))