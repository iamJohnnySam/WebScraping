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
    # "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
    # "download.extensions_to_open": "applications/pdf",
    # "safebrowsing.enabled": False
    })

import time
from random import random
from random import seed
seed(1)

from urllib.request import urlopen

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
    time.sleep(2*random())
    getter.find_element_by_name('request').send_keys(name)
    time.sleep(2*random())
    getter.find_element_by_id('open').click()
    
    soup2 = BS(getter.page_source, features="lxml")
    for a in soup2.find_all("a"):
        try:
            b = a['onclick'].replace("location.href='","")
            if ".pdf" in a:
                b = b.replace("?download=true'","")
                print (b)
        except:
            pass
        
        try:
            PDF = urlopen(b)
            with open(name+".pdf", 'wb') as file:
                file.write(PDF.read())
                file.close()
        except:
            getter.find_element_by_partial_link_text('save').click()
    
print ("End")
