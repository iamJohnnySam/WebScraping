scihub = "https://sci-hub.se/"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as BS

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\iamJohnnySam\\Desktop",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    })

import time

driver = webdriver.Chrome("chromedriver.exe")
getter = webdriver.Chrome("chromedriver.exe", options=chrome_options)

while True:
    inp = input("Enter the page you want downloaded: ") 
    
    if inp == "x":
        break
    
    driver.get(inp)
    time.sleep(3)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    if "ieeexplore.ieee.org/document/" in inp:
        name = soup.find_all("h1", class_="document-title")[0].text
    else:
        print("Unknown")
        break
    
    print ("You're downloading - " + name)
    
    getter.get(scihub)
    getter.find_element_by_name('request').click()
    getter.find_element_by_name('request').send_keys(name)
    getter.find_element_by_id('open').click()
    # time.sleep(1)
    # getter.find_element_by_id('open-button').click()
    
print ("End")
