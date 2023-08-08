import requests
from bs4 import BeautifulSoup
from webpage import babycentral as bbc
def PrintWebsiteData(search_Info):
    url = bbc.url(search_Info)
    response = requests.get(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    soup = BeautifulSoup(response.text, 'html.parser')
    bbc.extract(soup)