from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome("chromedriver.exe")

courses = []

def formatVal (temp):
    if "\xa0" in temp:
        temp = temp.replace("\xa0"," ")
    
    temp.strip()
    return temp

driver.get("https://london.northumbria.ac.uk/courses")
content = driver.page_source
soup = BS(content, features="lxml")

for val in soup.find_all("a", target="_blank"):
    print (formatVal(val.text))
