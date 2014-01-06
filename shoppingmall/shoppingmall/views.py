#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb

malls ={}

def hello(request):
	return HttpResponse('Hello ,django!')


def Malls(request):
	shoppingmall = [malls]

	page = request.path.split('/')

	print '页数' + page[2]

	db = MySQLdb.connect(host='localhost',user='root',passwd='',db='test',charset='utf8')
	cursor = db.cursor()
	cursor.execute('select * from shoppingmall')

	result = cursor.fetchall()
	shoppingmall.remove(malls) 

	i = 0
	for v in result:

		temp = {}
		temp["id"] = v[0]
		temp['name'] = v[1]
		temp['address'] = v[2]
		temp['phone'] = v[3]
		temp['city'] = v[4]
		temp['review'] = v[5][:16] + u'...'
		temp['longitude'] = v[6]
		temp['latitude'] = v[7]
		shoppingmall.append(temp)
		i=i +1

	cursor.close()
	i = int(page[2])
	print shoppingmall[1]['name']
	return render_to_response('shangchang.html',{'shoppingmall':shoppingmall[(i-1)*10:i*10-1]})

