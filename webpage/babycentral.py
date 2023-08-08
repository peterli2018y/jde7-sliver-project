from selenium.webdriver.common.by import By
import time

def url(search_Info):
    return f"https://babycentral.com.hk/zh/search?q={search_Info}&options%5Bprefix%5D=last"

def InitialData():
    keys=["productor", "product_name", "regular_price", "sale_price", "product_url", "size"]
    values=[[],[],[],[],[],0]
    return dict(zip(keys, values))

#I do not want to use selenium
""" 
def classText(finder_source, class_name):
    return finder_source.find_element(By.CLASS_NAME, class_name).text

def Location():
    dict_keys=list(InitialData().keys())
    loc_producer="Tag[ol]s"

    return dict(zip(keys, values))
    {"producer":


def extract(driver, , *args):
    chi_titles,producers,regular_prices, sale_prices, post_url=[],[],[],[],[]
    extracted = 0
    ol_result = driver.find_elements(By.TAG_NAME, 'ol')[1]
    for result_li in ol_result.find_elements(By.TAG_NAME, "li"):
        producer=classText(result_li, "price__vendor.price__vendor--listing").split("\n")[-1]
        producers.append(producer)
        
        chi_title=classText(result_li, "h4.grid-view-item__title.product-card__title")
        chi_titles.append(chi_title)
        
        regular_dollar_text=classText(result_li, "price-item.price-item--regular")
        regular_dollar=regular_dollar_text[3:].replace(",","")
        regular_prices.append(regular_dollar)

        sale_dollar_text=classText(result_li, "price-item.price-item--sale").split("\n")[-1]
        sale_dollar=sale_dollar_text[3:].replace(",","")
        sale_prices.append(sale_dollar)

        result_a=result_li.find_element(By.TAG_NAME, "a")
        post_url.append(result_a.get_attribute("href"))
        extracted += 1
    
    return producers,chi_titles,regular_prices,sale_prices,post_url,extracted

def nextPage(driver):
    result_li=driver.find_element(By.CLASS_NAME, "ais-Pagination-item.ais-Pagination-item--nextPage")
    a=result_li.find_element(By.TAG_NAME, "a")
    time.sleep(1)

    a.click() """

#bs4

def extract(soup):
    chi_titles,producers,regular_prices, sale_prices, post_url, extracted=[],[],[],[],[],0
    lis=soup.find_all('ol')
    print(len(lis))
    for li in lis:
        print(li)

"""
    ol_result = soup.find_elements(By.TAG_NAME, 'ol')[1]
    for result_li in ol_result.find_elements(By.TAG_NAME, "li"):
        producer=classText(result_li, "price__vendor.price__vendor--listing").split("\n")[-1]
        producers.append(producer)
        
        chi_title=classText(result_li, "h4.grid-view-item__title.product-card__title")
        chi_titles.append(chi_title)
        
        regular_dollar_text=classText(result_li, "price-item.price-item--regular")
        regular_dollar=regular_dollar_text[3:].replace(",","")
        regular_prices.append(regular_dollar)

        sale_dollar_text=classText(result_li, "price-item.price-item--sale").split("\n")[-1]
        sale_dollar=sale_dollar_text[3:].replace(",","")
        sale_prices.append(sale_dollar)

        result_a=result_li.find_element(By.TAG_NAME, "a")
        post_url.append(result_a.get_attribute("href"))
        extracted += 1
    
    return producers,chi_titles,regular_prices,sale_prices,post_url,extracted
"""