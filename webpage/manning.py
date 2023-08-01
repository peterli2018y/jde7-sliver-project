from my_selenium import openWedsite
from selenium.webdriver.common.by import By

#def search(search_Info):
 #   url=f"https://babycentral.com.hk/zh/search?q={search_Info}&bbchk_products%5BsortBy%5D=bbchk_products_price_high_to_low"
  #  driver=openWedsite(url)
  #  return driver

def run():
    url = "https://www.mannings.com.hk/mom-and-baby/baby-food/c/febabyfood"
    driver = openWedsite(url)
    results = driver.find_elements(By.XPATH, '//div[@class="product_listing product_grid"]')
    print(len(results))
    for result in results:
        print(result.text)
        print(result.text.split('\n'))
    