from my_selenium import importWebsite
import os
import sys
#import MyRequest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

search_Info="地毯"
def main():
    importWebsite("webpage", search_Info)

if __name__ == "__main__":
    main()
