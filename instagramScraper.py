#instagramScraper.py
import csv
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver 

url = 'https://www.instagram.com/p/BlWycAUHHR5/?taken-by=teasocietyofficial'

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/Users/michaelhau/Library/Application Support/Google/chromedriver', chrome_options=option)
browser.get(url)

buttonElement = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/a')
browser.execute_script("arguments[0].scrollIntoView()", buttonElement)
time.sleep(5)
browser.execute_script("window.scrollBy(0,-50)", "")
buttonElement.click()

innerHTML = browser.execute_script("return document.body.innerHTML")
bodySoup = BeautifulSoup(innerHTML,'html.parser')

listOfNames = []

for nameLi in bodySoup.findAll('li', attrs={'class':'gElp9'}):
	username = nameLi.div.div.div.a.text
	if username != "teasocietyofficial": #removes post owner from input
		listOfNames.append(username)

filteredListOfNames = []

for name in listOfNames:
	if name not in filteredListOfNames:
		filteredListOfNames.append(name)

print(listOfNames[random.randint(0,len(filteredListOfNames))])


