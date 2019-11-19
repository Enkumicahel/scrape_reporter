from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.ethiopianreporter.com" 

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get(BASE_URL + "/zena")
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
print("ddddddddd")

for h3 in soup.findAll('h3', href=False, attrs={'class':'post-title'}):
	for a in h3.findAll('a', href=True):
		print(BASE_URL + a.get('href'))
		driver.get(BASE_URL + a.get('href'))
		content = driver.page_source
		soup = BeautifulSoup(content, "lxml")
		for div in soup.findAll('div', href=False, attrs={'class':'field field--name-body field--type-text-with-summary field--label-hidden field__item'}):
			for p in div.findAll('p'):
				print(p.string)
				if p.string:
					with open('reporter_scrape.txt', 'a') as f:
						f.write(p.string + '\n')