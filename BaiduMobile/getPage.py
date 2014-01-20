# encoding: utf-8

import sys, urllib2
import urllib
import re
import bs4
import time

from urllib2 import Request, urlopen,URLError, HTTPError
from urllib import quote
from bs4 import BeautifulSoup

def fetchurl(url,count):

	req=urllib2.Request(url,None)

	print url

	req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML,like Gecko) Version/4.0 Mobile Safari/533")

	f=urllib2.urlopen(req)

	infoBody = f.read()

	soup = BeautifulSoup(infoBody)

	temp = soup.find_all(srcid='www_normal')

	string ={}
	i = count - 10

	for site in temp:
		i += 1
		string[i] = site.find_all('span','site')[0].string

	return string
 

def find4Web(Key):

	answer = {}
	try:
		for i in range(10,51,10):
			para = urllib.urlencode({'pn':i,'word':Key,'sa':'np','st':'111081'})
			print para
			UrlStr = "http://m.baidu.com/s?"+para
			answer.update( fetchurl(UrlStr,i))

			print answer

	except Exception,e:

		print e

	return answer
   

if __name__=="__main__":

	f = open("key.txt",'r')
	w = open("res.txt",'w')

	print '             Qv.                                                      \n             ZBjIjv;           ..,..                                  \n              @yizero.mFLIEmQ0qFFzSuFFZZqFSl;                         \n              yBzl;vvvczFIv;::,:,:::::::: @haohu.                     \n               BZFCvvvc;:,::;;;;;;;:;:;;;;     ;Zbu.                  \n               7BuNNv7;::;;;;:::,,,,,::::;;       IBO.                \n              .D0zFv7;::;:,.:;v7jjVyCslv;:::;.    .:jBF               \n             :BqVNvvv:::,;sCzZFuIysLsVzZZ0Fl;;:;;v;;,:0B              \n             bZVFlv7v,.vmOSBs           ..;bB0z:,;;;;:.jB             \n            @kevensun.SBv  BjQ:          vEEq VBl,:;;;:.jB            \n            BFzFs;7vvZb   sI  0b;      ;bF  B  ,BI,:;;;:.BV           \n            BFVFvvvvvB.   D.  ;bCm:  ;0Nb   N;  .B;:;;;;.lB           \n            bNzFvv7vlB.   BZ  q;  EO8F  R   Bj   #N.;;;;:;B           \n            0ByF7vvv;bF   BBBCb   @Wwz  7qSBBD   B7:;;;;,7B           \n         lRu7BNzV;vvvvBZ ;BBBBR ;B;  vB  bBBBB  BE,:;;;,,BZ           \n        Eb:. ;BFzj;vvv;0EBBBBB;:D     .#:RBBBBNRS,:;;;,:ZB            \n       mE.,,: ;REylvvvv;vLObBBbz        NBBBBDC;.:::::;EB,            \n       B..,:::..SbFc;vvvv;:;vCENZOZNFZNSy0s;.  ,,::;;IBB              \n       D8:.,:,,  ;O#F;;;vvv;;;;v7ljjyjsv;,,,;;;;v;vsRBl  ,vvvv;       \n        lDOl;vsu;  :jbF7;;;;;vvvvvvvvvvvvvvvvv;v7V8BV  ;bZsjsjzBl     \n          ;ySVlvEEc .BOBbZzlv;;;;;;;;;;;;;vvsjNEDbBl7suq;.,,,,.,B;    \n                 ,IZBQc8EF0R @guohezou.08DRDQ#BsZ0  ...,:::::,.Ez    \n                    BRV#OjzVFuDBbbbQENZZEZqSuLN8sqB.;;;,,,::::: DC    \n                    .ZOBQSzIcv;RZ.vyIVCClvvyVzZBqB#jCuVBs,.,,,.vb,    \n                       7#;v;v;;;0s     ;7qF:vvOQv,       @arqiao.     \n                       lq,;;;;;:EQ ;BEb  R7;;,Ss          ,:,,        \n                       LBjuVSVCOB ,BEB; zBsyFzBy                      \n                       uBzVFzzNB       ,BVmBbbBBc                     \n                       zBCuzuCBmvzZOQ8bBFO8v;;  7EC                   \n                       SBCICsLLVNZZZFFjIBF:;vv    #Z                  \n                       .RNFzzy @kexianli.:;;;v7;;,0b                  \n                            BEuuIBj    BOFCjcllyI#B.                  \n                            Bs;;;CB.   :@secbone.b                    \n                           RZvv7;;vQR    IBB#RbBy                     \n                          BZ;v7v,.. Bc     :vv;                       \n                          RL;;vv;;:;NZ                                \n                          Fmv7l7ssIjqBBqv                             \n                         NBBOzIVVSu0bBbBBB                            \n                         jBbBBBbBbBBBBBBBB                            \n                           .vuqQ8DQEZuc;                              \n\n'

	for keyWord in f:
		keyWord = keyWord.strip('\n')
		values = find4Web(keyWord)
		w.write("%s:\n"%(keyWord))
		for k,v in values.iteritems():
			w.write('%d\t%s\n'%(k,v))
		time.sleep(4)

	w.close()
	f.close()



