
from selenium.webdriver.common.by import By

def url(search_Info):
    return f"https://www.hktvmall.com/hktv/zh/search_a?keyword={search_Info}"

def extract(driver, data_size):
    result_divs=driver.find_elements(By.XPATH, '//div[@class="info-wrapper"]')
    titles=[]
    
    for info in result_divs:
        print(info.text.split("\n"))

    return {}