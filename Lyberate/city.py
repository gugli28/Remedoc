from bs4 import BeautifulSoup
import re
import urllib2
import MySQLdb
import string
import requests

# import socks
# import socket
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
# socket.socket = socks.socksocket


def fn (url):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	return soup
# url ='https://www.lybrate.com/city-index/'+str(num)
soup = BeautifulSoup (open('srcpg.html'))
print >>open('locality.txt','w'),''
option = soup.find_all('div',{'class':'span3'})
# print option
for item in option:
	print >>open('locality.txt','a'),item.a['href'].encode('ascii','ignore')