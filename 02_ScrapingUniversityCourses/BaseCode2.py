from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome("chromedriver.exe")

courses = []

def getSite (name, web, tag, value):
    driver.get(web)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    for val in soup.find_all(tag, class_=value):
        try:
            courses.append([name,val.text,val.contents[0].get('href')])
        except:
            pass
    
getSite ("Mancheseter", "https://www.manchester.ac.uk/study/undergraduate/courses/2021/", "div", "title")

print(courses)
