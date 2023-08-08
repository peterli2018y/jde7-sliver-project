
from selenium.webdriver.common.by import By

def url(search_Info):
    return f"https://www.hktvmall.com/hktv/zh/search_a?keyword={search_Info}"

def dollars2Float(dollar):
    float_str=dollar[2:].replace(",","")
    return float(float_str)
def InitialData():
    keys=["productor", "product_name", "regular_price", "sale_price", "product_url", "size"]
    values=[[],[],[],[],[],0]
    return dict(zip(keys, values))

def extract(driver, data_size):

    result_divs=driver.find_elements(By.XPATH, '//div[@class="info-wrapper"]')
    chi_titles, quanties, solds, rates, prices, discount_prices, producers=[], [], [], [], [], [],[]
    for info in result_divs:
        ProductName=info.find_element(By.CLASS_NAME, "brand-product-name").text
        chi_titles.append(ProductName)
        chi_titles.append(info.find_element(By.CLASS_NAME, "brand-product-name").text)
        quanties.append(result_ups[1])
        solds.append(result_ups[2])
        rates.append(result_ups[3])

        result_lowers=info.find_element(By.CLASS_NAME, "price-label").text.split("\n")
        prices.append(dollars2Float(result_lowers[0]))
        if len(result_lowers) > 1:
            discount_prices.append(dollars2Float(result_lowers[1]))
        else:
            discount_prices.append(dollars2Float(result_lowers[0]))

        result_a=info.find_element(By.TAG_NAME, 'a').text
        producers.append(result_a)
    
    data={"chi_title":chi_titles, "quanties":quanties, "solds":solds, "rates":rates, "prices":prices, 
            "discount_prices":discount_prices, "producers":producers}
    print(data)
    return data