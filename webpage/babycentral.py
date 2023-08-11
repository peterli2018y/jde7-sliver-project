from selenium.webdriver.common.by import By
from datetime import datetime

filenames = ["url_1.txt", "url_2.txt", "data.csv"]

def extract(driver):
    driver.get("https://babycentral.com.hk/zh/pages/brand")

    #discount
    hrefs=["https://babycentral.com.hk/zh/collections/deals"]

    brand_boxs = driver.find_elements(By.CLASS_NAME, "brand-box")
        
    for box in brand_boxs:
        href = box.find_element(By.TAG_NAME, "a").get_attribute("href")
        hrefs.append(href)
        print(href)
    
    for href in hrefs:
        data=searchProductWithUrl(driver, href)

def searchProductWithUrl(driver, url):
    driver.get(url)
    products=driver.find_elements(By.CLASS_NAME, "ais-Hits-item.grid__item.grid__item--collection-template.small--one-half.medium-up--one-quarter")
    print(len(products))

    

#Step 1:collect all brands url in "https://babycentral.com.hk/zh/pages/brand"