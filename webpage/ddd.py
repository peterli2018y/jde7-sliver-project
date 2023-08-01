from my_selenium import openWedsite
def run():
    search_Info ="奶粉"
    url=f"https://babycentral.com.hk/zh/search?q={search_Info}" 
    openWedsite(url)