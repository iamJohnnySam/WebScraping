from selenium import webdriver
from bs4 import BeautifulSoup as BS
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.daraz.lk/daraz-mall/")

content = driver.page_source
soup = BS(content, features="lxml")

price = []

#print(soup.find_all("div", class_="store-product"))
#print(soup.find_all("div", class_="store-product-price"))

c = 1
for val in soup.find_all("div", class_="store-product-price"):
    price.append(val.text)
    c +=1
    
print(price)