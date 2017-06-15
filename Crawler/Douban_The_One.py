import urllib.request
import ssl
import http.cookiejar
import gzip
import re
import math
import random
import string
import time
from bs4 import BeautifulSoup

cj=http.cookiejar.CookieJar()
httpshandler=urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))
httpcookieprocessor=urllib.request.HTTPCookieProcessor(cj)
#proxyhandler=urllib.request.ProxyHandler({'http':'http://123.7.31.205:808'})
opener=urllib.request.build_opener(httpshandler)

#获取当前用户页
for uid in range(1000001,147674899):
	url="https://www.douban.com/people/"+str(uid)+"/"
	print("URL "+url)
	header={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, sdch, br",
		"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		#"Cookie":"bid=%s"%"".join(random.sample(string.ascii_letters+string.digits,11)),
		"Host":"www.douban.com",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30"
	}
	#user_req=urllib.request.Request(url=user_href,headers=user_header)
	#user_response=opener.open(user_req)
	#user_gpage=user_response.read()
	#user_page=gzip.decompress(user_gpage).decode("utf-8")
	req=urllib.request.Request(url=url,headers=header)
	response=opener.open(req)
	gpage=response.read()
	page=gzip.decompress(gpage).decode("utf-8")
	soup=BeautifulSoup(page,"lxml")
	print(soup)
	#检查是否有共同爱好
	#print(user_soup.find_all(id="common"))
	#ex_common=user_soup.find_all(id="common")
	#if len(ex_common):
	#	common=ex_common.h2.string
	#	if re.search(r"(\d+)",common):
	#		common_num=re.findall(r"(\d+)",common)[0]
	#		common_num=common_num[1:-2]
	#		print("{0} SHARE {1} COMMONS WITH U".format(user_name,common_num))
	#time.sleep(0.1)
	break
	#if uid==1000101:break