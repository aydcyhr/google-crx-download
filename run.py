from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests

def geturl(url):
    res = requests.head(url)
    url = res.headers.get('location')
    return url

a = 1
with open('id.txt', 'r') as x:
	for line in x:
		id = line.replace('\n', '')
		url = 'http://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x='+id+'%26installsource%3Dondemand%26uc'
		new = geturl(url)
		print(new)
		r= requests.get(new)
		name = str(a)+'.crx'
		with open(name, "wb") as code:
			code.write(r.content) 
		a=a+1
