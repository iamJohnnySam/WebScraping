# https://johnsamarasinghe.blogspot.com/2020/12/scraping-university-courses-part-1.html

from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome("chromedriver.exe")

courses = []

def getSite (name, web, tag, value="none"):
    driver.get(web)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    if value == "none":
        for val in soup.find_all(tag):
            try:
                courses.append([name,val.text,val.contents[0].get('href')])
            except:
                pass
    else:
        for val in soup.find_all(tag, class_=value):
            try:
                courses.append([name,val.text,val.contents[0].get('href')])
            except:
                pass
        
    
getSite ("Mancheseter", "https://www.manchester.ac.uk/study/undergraduate/courses/2021/", "div", "title")
getSite ("Cambridge", "https://www.undergraduate.study.cam.ac.uk/courses", "h4")
getSite ("Cheseter", "https://www1.chester.ac.uk/course_atoz/52", "span", "table__primary")

print(courses)
