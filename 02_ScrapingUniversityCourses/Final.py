from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome("chromedriver.exe")

courses = []

def formatVal (temp):
    if "\xa0" in temp:
        temp = temp.replace("\xa0"," ")
    
    temp.strip()
    return temp

def getSite (name, web, tag, value="none", valType = "class"):
    driver.get(web)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    if value == "none":
        for val in soup.find_all(tag):
            try:
                courses.append([name,formatVal(val.text),web+val.contents[0].get('href')])
            except:
                pass
            
    elif valType == "class":
        for val in soup.find_all(tag, class_=value):
            try:
                courses.append([name,formatVal(val.text),web+val.contents[0].get('href')])
            except:
                pass
            
    elif valType == "target":
        for val in soup.find_all(tag, target=value):
            try:
                courses.append([name,formatVal(val.text),web+val.contents[0].get('href')])
            except:
                pass
            
    else:
        print("Error")
        
   
getSite ("University of Mancheseter", "https://www.manchester.ac.uk/study/undergraduate/courses/2021/", "div", "title")
getSite ("University of Cambridge", "https://www.undergraduate.study.cam.ac.uk/courses", "h4")
getSite ("University of Hertfordshire", "https://www.herts.ac.uk/international/new-international-students/intakes/january-2021-courses", "th")
getSite ("University of Cheseter", "https://www1.chester.ac.uk/course_atoz/52", "span", "table__primary")
getSite ("Bangor University", "https://www.bangor.ac.uk/international/courses/january-start", "li")

#getSite ("Ulster University", "https://www.ulster.ac.uk/courses?&f.Level_u%7CY=Postgraduate", "h3", "h2 bl")

#getSite ("Northumbria University - London", "https://london.northumbria.ac.uk/courses","a", "_blank", "target")
#getSite ("University of Roehampton",
#getSite ("Solent University",
#getSite ("University of Essex",

print(courses)


import csv

with open('output.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, delimiter=',')
    for a in courses:
        print(a)
        wr.writerow(a)
