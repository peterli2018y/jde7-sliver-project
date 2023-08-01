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

def importWebsite(folder_path):
    for file_name in os.listdir(folder_path):
    # Check that the file is a Python file
        if file_name.endswith('.py'):
            # Get the module name (without the .py extension)
            module_name = file_name[:-3]
            # Import the module dynamically
            module = importlib.import_module(f'{folder_path}.{module_name}')
            # Use the module
            module.run("奶粉")