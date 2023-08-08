import os
import importlib
import time
#import pandas as pd
from selenium import webdriver

def openWedsite(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        return driver
    except:
        print("invail url!")
        return None
def importWebsite(folder_path, search_Info):
    for file_name in os.listdir(folder_path):
    # Check that the file is a Python file
        if file_name.endswith('.py'):
            # Get the module name (without the .py extension)
            module_name = file_name[:-3]
            # Import the module dynamically
            module = importlib.import_module(f'{folder_path}.{module_name}')
            # Use the module

            data=module.InitialData()
            page_url=module.url(search_Info)
            driver=openWedsite(page_url)
            for page in range(1,4):
                raw_data=module.extract(driver)
                for key, value in zip(list(data.keys()), list(raw_data)):
                    data[key] += value
                page_url=module.nextPage(driver)
                if page_url == "":break
            print(data["size"])