#!/usr/bin/python
# coding: utf-8

import requests, os, time, sys
from bs4 import BeautifulSoup


class getBook():
	def __init__(self, url):
		self.url = url

	def _get_page_soup(self, url):
		web_data=requests.get(url)
		web_data.encoding = "GBK"
		soup=BeautifulSoup(web_data.text)
		return soup

	def _get_page_soup_html(self, html_doc):
		soup = BeautifulSoup(html_doc, 'html.parser')
		return soup

	def get_book_title(self, url):
		soup = self._get_page_soup(url)
		book_title= str(soup.find("title")).split(">")[1].split("- 小说")[0]
		return book_title		

	def get_book_short_intro(self, url):
		soup = self._get_page_soup(url)
		parser_soup = self._get_page_soup_html(str(soup))
		print parser_soup.find_all('tr')
		#short_intro = str(soup.find("td"))
		#print short_intro


	def get_page_title(self, url):
		soup = self._get_page_soup(url)
		page_title= str(soup.find("font")).split(">")[1].split("<")[0]
		return page_title


	def get_page_context(self, bookid, pageid):
		text=""
		url="http://www.kanunu8.com/book3/%d/%d.html"%(bookid,pageid)

		soup = self._get_page_soup(url)
		td= soup.find("td", width="820")
		td_tag=list(td)[1]
		for tag in td_tag.find_all('br'):
		    tag.replaceWith('')
		chapter_content = str(td_tag).replace('<p>','').replace('</p>','')
		return chapter_content

	def get_page_title_and_content(self):
		page_title = self.page_title(url)
		chapter_content = self.chapter_content(bookid, pageid)
		return '\n\n\n\n' + page_title + '\n\n' + chapter_content + '\n\n'



	def get_book_chapters(self, content, start, end):
		i = 1
		for pageid in range(start, end):
			try:
				print 'Chapter' + str(i)
				content = content + str(self.get_page_title_and_content(bookid,pageid))
				i = i+1
			except Exception,e:
				print "ignore page error: "+str(pageid)
				print e
				continue
		return content












if __name__ == '__main__':
	## this book is scraped from http://www.kanunu8.com/files/writer/4208.html

	book = getBook("http://www.kanunu8.com/tuili/9498/")
	bookname = book.get_book_title(book.url)
	book.get_book_short_intro(book.url)


#	bookid = 6862
#	start = start_page = 131385
#	end_page = 131394
	
#	content = bookname
#	print os.getcwd()
#	f = open(bookname, 'w')
#	end = end_page + 1

#	content = get_book_chapters
#	f.write(content)
#	f.close()

