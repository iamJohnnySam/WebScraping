from selenium import webdriver
from bs4 import BeautifulSoup as BS
import numpy as np

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://goldprice.org/gold-price-history.html#All%20Data")

content = driver.page_source
soup = BS(content, features="lxml")

#valueString = soup.find_all('path', class_='highcharts-area')[0]['d']
valueString = soup.find_all('path')[66]['d']

comValues = valueString.split(" L ")

values = np.zeros([1, 2])

for x in comValues:
    temp = x.split(" ")
    if temp[0] == 'M':
        temp.remove('M')
        
    temp = [float(i) for i in temp]
    
    if (values [0][1] == 0):
        values [0][0] = temp [0]
        values [0][1] = temp [1]
    else:
        temp = np.array(temp).reshape((1, 2))
        values = np.append(values, temp, axis = 0)
    
print (values)
