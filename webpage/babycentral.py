from my_selenium import openWedsite
from selenium.webdriver.common.by import By

def search(search_Info):
    url=f"https://babycentral.com.hk/zh/search?q={search_Info}&bbchk_products%5BsortBy%5D=bbchk_products_price_high_to_low"
    driver=openWedsite(url)
    return driver

def run(search_Info):
    #driver = search(search_Info)
    #result04=driver.find_elements(By.XPATH, "//li")
    pass