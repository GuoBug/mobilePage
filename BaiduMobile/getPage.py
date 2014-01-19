# encoding: utf-8

import sys, urllib2
import urllib
import re
import bs4
import time

from urllib2 import Request, urlopen,URLError, HTTPError
from urllib import quote
from bs4 import BeautifulSoup

def fetchurl(url):

	req=urllib2.Request(url,None)

	print url

	req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML,like Gecko) Version/4.0 Mobile Safari/533")

	f=urllib2.urlopen(req)

	infoBody = f.read()

	soup = BeautifulSoup(infoBody)

	temp = soup.find_all(srcid='www_normal')

	string =[]

	for site in temp:
		string.append( site.find_all('span','site')[0].string)

	return string
 

def test(Key):

	try:
		for i in range(10,51,10):
			para = urllib.urlencode({'pn':i,'word':Key,'sa':'np','st':'111081'})
			print para
			UrlStr = "http://m.baidu.com/s?"+para
			print fetchurl(UrlStr)

	except Exception,e:

		print e

   

if __name__=="__main__":

	f = open("key.txt",'r')

	for keyWord in f:
		keyWord = keyWord.strip('\n')
		test(keyWord)
		time.sleep(10)