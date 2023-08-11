import os
import importlib
import time
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def importWebsite(folder_path, search_Info):
    driver = webdriver.Chrome()
    for file_name in os.listdir(folder_path):
    # Check that the file is a Python file
        if file_name.endswith('.py'):
            # Get the module name (without the .py extension)
            module_name = file_name[:-3]
            # Import the module dynamically
            module = importlib.import_module(f'{folder_path}.{module_name}')
            # Use the module
            module.extract(driver)