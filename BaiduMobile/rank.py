# encoding: utf-8

import sys, urllib2
import urllib
import bs4
import time
import threading
import xlwt #excel
import Queue

from urllib2 import Request, urlopen,URLError, HTTPError
from urllib import quote
from random import choice
from bs4 import BeautifulSoup


f = open("4rank.txt",'w')
all50 = open("top50.txt",'w')
filetop = False  #False 表示可写
file4 = False
fileLineCount = 1 #防止写文件串行
keyQueue = Queue.Queue(0) #key的 FIFO
requestInfo = {
	"Host":"www.baidu.com",
	"Referer":"http://www.baidu.com/?from=844b&ms=1",
	"User-Agent":"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML,like Gecko) Version/4.0 Mobile Safari/533"
}
ipList = ["113.57.252.106:80","119.97.146.16:80","61.54.221.200:3128"]

#取出关健词
def fetchurl(url,urlRank):

	req=urllib2.Request(url,None)
	ip = choice(ipList)
	print url+"Ip :" + ip

	#定义请求头
	for k in requestInfo:
		req.add_header(k,requestInfo[k])

	proxy_handler = urllib2.ProxyHandler({'http': 'http://'+ip})
	opener = urllib2.build_opener(proxy_handler)
	urllib2.install_opener(opener)
	f=urllib2.urlopen(req)

	#取得网页内容
	infoBody = f.read()
	soup = BeautifulSoup(infoBody)

	#找到关健词的位置
	temp = soup.find_all(srcid='www_normal')
	for site in temp:
		urlRank.append(site.find_all('span','site')[0].string)


class GetBaiduRank(threading.Thread):
	"""docstring for GetBaiduRank"""
	def __init__(self):
		super(GetBaiduRank, self).__init__()
		self.local = threading.local()
		global filetop,file4,keyQueue

	def run(self):
		self.local.urlRank = []
		global fileLineCount
		#空，词取完了
		if keyQueue.empty():
			return

		#取词
		keyWord = keyQueue.get()
		#此行被占用，换行
		fileline = fileLineCount
		fileLineCount = fileLineCount + 1

		fileExcel = xlwt.Workbook()
		sheet = fileExcel.add_sheet('key word')
		excelLine = 0
		mainRank = ['0','0','0','0']

		for i in range(10,51,10):
			print i
			para = urllib.urlencode({'pn':i,'word':keyWord,'sa':'np','st':'11104i'})
			urlStr = "http://m.baidu.com/s?"+para
			fetchurl(urlStr,self.local.urlRank)
			self.local.urlRank = list(set(self.local.urlRank))

		for web in self.local.urlRank:
			while filetop == True:
				time.sleep(1)

			filetop == True
			all50.write(str(fileline)+"\t"+str(self.local.urlRank.index(web))+"\t"+web+"\n")
			filetop == False


			try:
				sheet.write(fileline,self.local.urlRank.index(web) ,web)
				fileExcel.save('demo.xls')
			except Exception,e:
				print e
			if cmp(web , "m.ctrip.com") == 0:
				mainRank[0] = str(self.local.urlRank.index(web) + 1)
			if cmp(web , "m.elong.com") == 0:
				mainRank[1] = str(self.local.urlRank.index(web) + 1)
			if cmp(web, "touch.17u.cn") == 0:
				mainRank[2] = str(self.local.urlRank.index(web) + 1)
			if cmp(web, "touch.qunar.com") == 0:
				mainRank[3] = str(self.local.urlRank.index(web) + 1)

		while file4 == True:
			time.sleep(1)
		print "写 file 4"
		file4 == True
		f.write(keyWord+":\n")
		f.write("\t".join(mainRank))
		f.write("\n")
		file4 == False



if __name__ == '__main__':

	print '             Qv.                                                      \n             ZBjIjv;           ..,..                                  \n              @yizero.mFLIEmQ0qFFzSuFFZZqFSl;                         \n              yBzl;vvvczFIv;::,:,:::::::: @haohu.                     \n               BZFCvvvc;:,::;;;;;;;:;:;;;;     ;Zbu.                  \n               7BuNNv7;::;;;;:::,,,,,::::;;       IBO.                \n              .D0zFv7;::;:,.:;v7jjVyCslv;:::;.    .:jBF               \n             :BqVNvvv:::,;sCzZFuIysLsVzZZ0Fl;;:;;v;;,:0B              \n             bZVFlv7v,.vmOSBs           ..;bB0z:,;;;;:.jB             \n            @kevensun.SBv  BjQ:          vEEq VBl,:;;;:.jB            \n            BFzFs;7vvZb   sI  0b;      ;bF  B  ,BI,:;;;:.BV           \n            BFVFvvvvvB.   D.  ;bCm:  ;0Nb   N;  .B;:;;;;.lB           \n            bNzFvv7vlB.   BZ  q;  EO8F  R   Bj   #N.;;;;:;B           \n            0ByF7vvv;bF   BBBCb   @Wwz  7qSBBD   B7:;;;;,7B           \n         lRu7BNzV;vvvvBZ ;BBBBR ;B;  vB  bBBBB  BE,:;;;,,BZ           \n        Eb:. ;BFzj;vvv;0EBBBBB;:D     .#:RBBBBNRS,:;;;,:ZB            \n       mE.,,: ;REylvvvv;vLObBBbz        NBBBBDC;.:::::;EB,            \n       B..,:::..SbFc;vvvv;:;vCENZOZNFZNSy0s;.  ,,::;;IBB              \n       D8:.,:,,  ;O#F;;;vvv;;;;v7ljjyjsv;,,,;;;;v;vsRBl  ,vvvv;       \n        lDOl;vsu;  :jbF7;;;;;vvvvvvvvvvvvvvvvv;v7V8BV  ;bZsjsjzBl     \n          ;ySVlvEEc .BOBbZzlv;;;;;;;;;;;;;vvsjNEDbBl7suq;.,,,,.,B;    \n                 ,IZBQc8EF0R @guohezou.08DRDQ#BsZ0  ...,:::::,.Ez    \n                    BRV#OjzVFuDBbbbQENZZEZqSuLN8sqB.;;;,,,::::: DC    \n                    .ZOBQSzIcv;RZ.vyIVCClvvyVzZBqB#jCuVBs,.,,,.vb,    \n                       7#;v;v;;;0s     ;7qF:vvOQv,       @arqiao.     \n                       lq,;;;;;:EQ ;BEb  R7;;,Ss          ,:,,        \n                       LBjuVSVCOB ,BEB; zBsyFzBy                      \n                       uBzVFzzNB       ,BVmBbbBBc                     \n                       zBCuzuCBmvzZOQ8bBFO8v;;  7EC                   \n                       SBCICsLLVNZZZFFjIBF:;vv    #Z                  \n                       .RNFzzy @kexianli.:;;;v7;;,0b                  \n                            BEuuIBj    BOFCjcllyI#B.                  \n                            Bs;;;CB.   :@secbone.b                    \n                           RZvv7;;vQR    IBB#RbBy                     \n                          BZ;v7v,.. Bc     :vv;                       \n                          RL;;vv;;:;NZ                                \n                          Fmv7l7ssIjqBBqv                             \n                         NBBOzIVVSu0bBbBBB                            \n                         jBbBBBbBbBBBBBBBB                            \n                           .vuqQ8DQEZuc;                              \n\n'

	threads = []
	sourceFile = open('key.txt','r')

	for keyWord in sourceFile:
		#去掉换行
		keyWord = keyWord.strip('\n')
		#sheet.write(excelLine,0,keyWord)
		keyQueue.put(keyWord)

	for i in range(5):
		k = GetBaiduRank()
		k.setDaemon(True)
		k.start()
		threads.append(k)

	for t in threads:
		t.join()
f.close()

 