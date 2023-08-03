from selenium.webdriver.common.by import By

def url(search_Info):
    return f"https://babycentral.com.hk/zh/search?q={search_Info}&bbchk_products%5BsortBy%5D=bbchk_products_price_high_to_low"

def extract(driver, required_data_size=60, current_size=0):
    result_ol=driver.find_elements(By.TAG_NAME, "ol")[1]
    i,j= 0,0
    en_titles,producers,prices, post_url=[],[],[], []
 
    for result_li in result_ol.find_elements(By.TAG_NAME, "li"):
        for text in result_li.text.split("\n"):
            if j == 0:
                en_titles.append(text)
            elif j == 3:
                producers.append(text)
            elif j == 6:
                #remove "HK$ "from "HK$ 100"
                prices.append(float(text[4:].replace(",","")))
            j +=1

        j = 0
        i += 1 
        result_a=result_li.find_element(By.TAG_NAME, "a")
        post_url.append(result_a.get_attribute("href"))

    current_size += i
    if required_data_size > current_size:
        try:
            next_page = driver.find_element(By.CLASS_NAME, '//a[@class="ais-Pagination-link"]')
            next_page.click()
            data = extract(driver, required_data_size, current_size)
            en_titles += data["en_title"]
            producers += data["producer"]
            prices += data["price"]
            post_url += data["post_url"]
        except:
            print(f"A maximum of {current_size} found!")
        finally:
            return {"en_title":en_titles,"producer":producers,"price":prices, "post_url":post_url}
    return {"en_title":en_titles,"producer":producers,"price":prices, "post_url":post_url}