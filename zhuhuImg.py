# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from urllib import parse,request
import json


def craw(id):
	header = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36",
	    "Referer": "https://www.zhihu.com/question/"+str(id),
	    "authorization": "Bearer Mi4wQUJBTXlHRk9ad2dBVUlMZTFaU3ZDeGNBQUFCaEFsVk5XREV5V1FCcmN6MHhtQXFxdUt1UXlMWWRxYjF6eE9sMHlR|1493872282|d3c61e09cc03de29919ccde52af9bceea08c2b7d"
	}


	imgPage = 1
	offset = 0
	while(offset < 24):
		url = 'https://www.zhihu.com/api/v4/questions/'+str(id)+'/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset='+str(offset)
		req = request.Request(url, headers = header)
		response = request.urlopen(req)
		html_doc = response.read()
		jsonObj = json.loads(html_doc)

		dataPage = 0
		try:
			while(dataPage < 20):
				html = jsonObj.get("data")[dataPage].get("content")
				bsObj = BeautifulSoup(html, 'html.parser')
				dataList = bsObj.findAll(name = 'img', attrs = 
					{'data-rawwidth':re.compile(r'\d{0,4}'), 'src':re.compile(r'https://')})

				for data in dataList:
					# print(data.attrs['src'])
					with open('img/' + str(imgPage) +'.jpg', 'wb') as w:
						w.write(request.urlopen(data.attrs['src']).read())
						print("第 "+str(imgPage)+" 张图片")
						imgPage = imgPage+1
				dataPage = dataPage+1
		except Exception as e:
			print(e)
		
		
		offset = offset+20

craw(28467579)


# url = 'https://www.zhihu.com/question/22918070'
# html_doc = request.urlopen(url)
# html = html_doc.read()
# bsObj = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
# dataList = bsObj.findAll(name = 'img', attrs = 
# 	{'data-rawwidth':re.compile(r'\d{0,4}'), 'src':re.compile(r'https://')})

# imgPage = 1

# try:
# 	for data in dataList:
# 		with open('img/' + str(imgPage) +'.jpg', 'wb') as w:
# 			w.write(request.urlopen(data.attrs['src']).read())
# 			print("第 "+str(imgPage)+" 张图片")
# 			imgPage = imgPage+1
# except Exception as e:
# 	print(e)















