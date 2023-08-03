from my_selenium import openWedsite
from selenium.webdriver.common.by import By

def url(search_Info):
    return f"https://www.hktvmall.com/hktv/zh/search_a?keyword={search_Info}"

def extract(driver):
    return{}