from re import search
from my_selenium import openWedsite
from selenium.webdriver.common.by import By

def url(search_Info):
    return f"https://babycentral.com.hk/zh/search?q={search_Info}&bbchk_products%5BsortBy%5D=bbchk_products_price_high_to_low"

def extract(driver):
    result_ol=driver.find_elements(By.TAG_NAME, "ol")[1]
    #ol->li->divs->text
    i,j= 0,0
    en_titles,producers,prices, post_url=[],[],[], []
    for result_li in result_ol.find_elements(By.TAG_NAME, "li"):
        for text in result_li.text.split("\n"):
            print(text)
            if j == 0:
                en_titles.append(text)
            elif j == 3:
                producers.append(text)
            elif j == 6:
                prices.append(text)
            j +=1

        j = 0
        i += 1 
        result_a=result_li.find_element(By.TAG_NAME, "a")
        post_url.append(result_a.get_attribute("href"))

    return {"en_title":en_titles,"producer":producers,"price":prices, "post_url":post_url}

