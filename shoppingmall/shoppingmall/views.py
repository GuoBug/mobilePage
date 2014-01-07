#encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb

malls ={}

def hello(request):
	return HttpResponse('Hello ,django!')

#全部
def Malls(request):
	shoppingmall = [malls]

	page = request.path.split('/')

	print '页数' + page[2]

	i = int(page[2])

	shoppingmall = DbSelect(1,'0')
	topTen = DbSelect(2,'top')

	print shoppingmall[1]
	return render_to_response('shangchang.html',{'shoppingmall':shoppingmall[(i-1)*10:i*10-1],'topTen':topTen})

#单个
def ShowDetail(request):
	info =request.path.split('/')

	print '商场编号' + info[2]

	mallInfo = DbSelect(2,info[2])
	topTen = DbSelect(2,'top')

	return render_to_response('mallDetail.html',{'mallInfo':mallInfo[0],'topTen':topTen})

#城市
def ShowCity(request):
	info =request.path.split('/')

	print '商场编号' + info[3]

	cityInfo = DbSelect(2,info[3])
	topTen = DbSelect(1,'top')

	i = int(info[2])

	return render_to_response('shangchang.html',{'shoppingmall':cityInfo[(i-1)*10:i*10-1],'topTen':topTen})

# 操作数据库
def DbSelect(id,instring):
	shoppingmall = [malls]

	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset='utf8')
	cursor = db.cursor()


	if (id == 1):
		if (instring !='0' ):
			print 'var is exist'
			cursor.execute('select * from shoppingmall where city=\'' + instring + '\'')
		else:
			print 'no var'
			cursor.execute('select * from shoppingmall')
	if (id == 2):
		if (instring != 'top'):
			cursor.execute('select * from shoppingmall where Id =\'' + instring +'\'')
		else:
			cursor.execute('select * from shoppingmall order by id desc limit 10')

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
		temp['longitude'] = v[6]
		temp['latitude'] = v[7]
		if (id == 1):
			temp['review'] = v[5][:16] + u'...'
		else:
			temp['review'] = v[5]
		shoppingmall.append(temp)

	return shoppingmall
