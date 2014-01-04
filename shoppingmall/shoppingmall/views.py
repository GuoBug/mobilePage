#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb

malls ={}

def hello(request):
	return HttpResponse('Hello ,django!')


def Malls(request):
	shoppingmall = [malls]

	db = MySQLdb.connect(host='localhost',user='root',passwd='',db='test',charset='utf8')
	cursor = db.cursor()
	cursor.execute('select * from shoppingmall')

	result = cursor.fetchall()
	shoppingmall.remove(malls) 

	i = 0
	for v in result:

		temp = {}
		temp['name'] = v[1][:10]
		temp['address'] = v[2][:8]
		temp['phone'] = v[3][:12]
		temp['city'] = v[4]
		temp['review'] = v[5][:16] + u'...'
		temp['longitude'] = v[6]
		temp['latitude'] = v[7]
		shoppingmall.append(temp)
		i=i +1

	cursor.close()
	print shoppingmall[1]['name']
	return render_to_response('shangchang.html',{'shoppingmall':shoppingmall})