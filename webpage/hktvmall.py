from my_selenium import openWedsite
from selenium.webdriver.common.by import By

def search(search_Info):
    url=f"https://www.hktvmall.com/hktv/zh/search_a?keyword={search_Info}"
    driver=openWedsite(url)
    return driver

def run():
    driver = search("奶粉")
    

