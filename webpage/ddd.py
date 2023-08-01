import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def openWedsite(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        return driver
    except:
        print("invail url!")
        return None
 