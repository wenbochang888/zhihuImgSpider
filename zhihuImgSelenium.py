# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request
from bs4 import BeautifulSoup 
import re
import time

url = 'https://www.zhihu.com/question/50734809'
driver = webdriver.Firefox()
# driver = webdriver.PhantomJS(executable_path = "img/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get(url)
try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//button[@class='Button QuestionMainAction']")))
except Exception as e:
	print(e)
finally:
	button = driver.find_element_by_xpath("//button[@class='Button QuestionMainAction']")
	print(button.text)
	button.click()
	html = driver.page_source
html = driver.page_source
# html = html.replace("lt;", "<")
# html = html.replace("gt;", "</img>") 


bsObj = BeautifulSoup(html, 'html.parser')
dataList = bsObj.findAll(name = 'img', attrs = 
	{'data-rawwidth':re.compile(r'\d{0,4}'), 'data-original':re.compile(r'https://')})
page = 1
for data in dataList:
	print(data.attrs['data-original'])
	print("\n-----"+ str(page) +"-------\n")
	page = page + 1

imgPage = 1
for data in dataList:
	pass
	with open('img2/' + str(imgPage) +'.jpg', 'wb') as w:
		w.write(request.urlopen(data.attrs['data-original']).read())
		print("第 "+str(imgPage)+" 张图片")
		imgPage = imgPage + 1












