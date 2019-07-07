#! python3

# setting up modules for web requests and parsing

import requests 
from bs4 import BeautifulSoup

url = 'https://courses.edx.org/courses/course-v1:UTAustinX+UT.6.10x+2T2018/course/'  # url string storage 
page = requests.get(url)    # assining the extracted url to a var
soup = BeautifulSoup(page.text,'html.parser')
with open('soup.txt','w', encoding = 'utf-8') as fileId:
    fileId.write(soup.prettify())

