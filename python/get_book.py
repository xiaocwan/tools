#!/usr/bin/python
# coding: utf-8

import requests, os, time, sys
from bs4 import BeautifulSoup

def get_context_from_page(bookid,pageid):
	text=""
	url="http://www.kanunu8.com/book/%d/%d.html"%(bookid,pageid)
	web_data=requests.get(url)
	web_data.encoding = "GBK"
	soup=BeautifulSoup(web_data.text)

	chapter_title= str(soup.find("font")).split(">")[1].split("<")[0]

	td= soup.find("td", width="820")
	td_tag=list(td)[1]
	for tag in td_tag.find_all('br'):
	    tag.replaceWith('')
	chapter_content = str(td_tag).replace('<p>','').replace('</p>','')

	return '\n\n\n\n' + chapter_title + '\n\n' + chapter_content + '\n\n'

if __name__ == '__main__':
	## this book is scraped from http://www.kanunu8.com/files/writer/4208.html
	bookname = "坚硬如水 - 阎连科"
	start = bookid = 4213
	start_page = 46355
	end_page = 46369
	
	content = bookname
	print os.getcwd()
	f = open(bookname, 'w')
	i = 1
	end = end_page + 1
	for pageid in range(start_page, end):
		try:
			print 'Chapter' + str(i)
			content = content + str(get_context_from_page(bookid,pageid))
			i = i+1
		except Exception,e:
			print "ignore page error: "+str(pageid)
			print e
			continue
	f.write(content)
	f.close()

