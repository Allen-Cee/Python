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
https_tlsv1_handler=urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))
opener=urllib.request.build_opener(https_tlsv1_handler)
#print("ENTER TARGET LINK: ")
tar_url="https://book.douban.com/subject/1477396/"
url=tar_url+"collections?start="
total_pagenum=0

#获取当前评价用户页
for start in range(0,200,20):
	cur_url=url+str(start)
	header={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, sdch, br",
		"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
		"Connection":"keep-alive",
		"Host":"book.douban.com",
		"Referer":cur_url,
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	}
	req=urllib.request.Request(url=cur_url,headers=header)
	response=opener.open(req)
	gpage=response.read()
	page=gzip.decompress(gpage).decode("utf-8")
	soup=BeautifulSoup(page,"lxml")

	total_page_num=math.ceil(int(re.findall(r'\d+',soup.find_all("div",class_="article")[0].h2.span.string)[0])/20)
	page_num=0 if start==0 else int(start/20)
	print("PROCESSING PAGE {0} -- {1:>4.1f}%".format(page_num,page_num*100/total_page_num))

	#处理当前用户
	users_list=soup.find_all("div",class_="sub_ins")[0].find_all("table")
	count=0
	for user in users_list:
		count+=1
		user_name=user.find_all("div",class_="pl2")[0].a.find_all("span")[0].string
		user_href=user.find_all("div",class_="pl2")[0].a["href"]
		print("CHECKING USER {0}-{1:0>2} {2}".format(page_num,count,user_name))

		user_header={
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, sdch, br",
			"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
			"Cache-Control":"max-age=0",
			"Connection":"keep-alive",
			"Cookie":"bid=%s"%"".join(random.sample(string.ascii_letters+string.digits,11)),
			"Host":"www.douban.com",
			"Referer":tar_url+"collections",
			"Upgrade-Insecure-Requests":"1",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
		}
		#user_req=urllib.request.Request(url=user_href,headers=user_header)
		#user_response=opener.open(user_req)
		#user_gpage=user_response.read()
		#user_page=gzip.decompress(user_gpage).decode("utf-8")
		user_req=urllib.request.Request(url=user_href,headers=user_header)
		user_page=urllib.request.urlopen(user_req,context=ssl.SSLContext(ssl.PROTOCOL_TLSv1)).read().decode("utf-8")
		user_soup=BeautifulSoup(user_page,"lxml")

		#检查是否有共同爱好
		print(user_soup.find_all(id="common"))
		ex_common=user_soup.find_all(id="common")
		if len(ex_common):
			common=ex_common.h2.string
			if re.search(r"(\d+)",common):
				common_num=re.findall(r"(\d+)",common)[0]
				common_num=common_num[1:-2]
				print("{0} SHARE {1} COMMONS WITH U".format(user_name,common_num))
		time.sleep(0.1)

	next_href=soup.find_all("div",class_="paginator")[0].find_all("span",class_="next")
	if(len(next_href)==0):break
	print("\n")