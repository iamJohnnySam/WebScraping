from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time

driver = webdriver.Chrome("chromedriver.exe")

inp = [9424,8425306,7756,19,5326,7361,7083369,6221021,6221020,34,6221037,6287639,6221036,6221037,3468,7361]
inp = list(dict.fromkeys(inp))
out = []

for x in inp:
    web = "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber="+str(x)
    
    driver.get(web)
    time.sleep (3)
    content = driver.page_source
    soup = BS(content, features="lxml")
    
    name = soup.find_all("h1")[0].text
    
    try:
        impact = soup.find_all("a", class_="stats-jhp-impact-factor")[0].text
        impact = impact.replace(" Impact Factor","")
    except:
        impact = "Not Found"
    
    try:
        eigen = soup.find_all("a", class_="stats-jhp-eigenfactor")[0].text
        eigen = eigen.replace(" Eigenfactor","")
    except:
        eigen = "Not Found"
        
    desc = soup.find_all("span", class_="aims-scope-container")[0].text
    desc = desc.replace("  ","")
    desc = desc.strip()

    out.append([name, web, impact, eigen, desc])
    
    print(name + " - done")
    
import csv

with open('output.csv', 'w', newline='', encoding="utf-8") as myfile:
    wr = csv.writer(myfile, delimiter=',')
    for a in out:
        wr.writerow(a)
