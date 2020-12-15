from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome("chromedriver.exe")

def getSite (web, tag, value):
    driver.get(web)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    for val in soup.find_all(tag, class_=value):
        print(val.text)
    print("----------------------------------------------")
    
getSite ("https://www.manchester.ac.uk/study/undergraduate/courses/2021/", "div", "title")
