#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb



def hello(request):
	return HttpResponse('Hello ,django!')


def Malls(request):
	shoppingmall = {'name':'',
                  'address':'',
                  'phone':'',
                  'city':'',
                  'review':'',
                  'longitude':'',
                  'latitude':''
                  }

	db = MySQLdb.connect(host='localhost',user='root',passwd='',db='test',charset='utf8')
	cursor = db.cursor()
	cursor.execute('select * from shoppingmall')

	result = cursor.fetchall()

	i = 0
	for v in result:

	#	shoppingmall[i] = {}
	#	shoppingmall[i]['name'] = v[1]
	#	shoppingmall[i]['address'] = v[2]
	#	shoppingmall[i]['phone'] = v[3]
	#	shoppingmall[i]['city'] = v[4]
	#	shoppingmall[i]['review'] = v[5]
	#	shoppingmall[i]['longitude'] = v[6]
	#	shoppingmall[i]['latitude'] = v[7]
	#	print shoppingmall[i]['name'].encode("utf8")

		i=i +1

	cursor.close()
	print v
	shoppingmall = {}
	shoppingmall['name'] = v[1]
	shoppingmall['address'] = v[2]
	shoppingmall['phone'] = v[3]
	shoppingmall['city'] = v[4]
	shoppingmall['review'] = v[5]
	shoppingmall['longitude'] = v[6]
	shoppingmall['latitude'] = v[7]
	print shoppingmall
	return render_to_response('shangchang.html',{'shoppingmall':shoppingmall})