import urllib.request
import gzip
import http.cookiejar
import re
import time
from bs4 import BeautifulSoup

header={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Host":"copper.ccmn.cn",
	"Referer":"http://copper.ccmn.cn/copperprice/cjxh/?offset=80",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

for page_num in range(0,1501,20):
	root_url="http://copper.ccmn.cn/copperprice/cjxh/?offset="+str(page_num)
	root_page=urllib.request.urlopen(root_url).read().decode("gb2312")
	root_soup=BeautifulSoup(root_page,"lxml")
	news=root_soup.find_all("td",class_="news")
	for td in news:
		href=td.find_all("a")[0]["href"]
		url="http://copper.ccmn.cn"+href
		req=urllib.request.Request(url=url,headers=header)
		response=opener.open(req)
		gpage=response.read()
		page=gzip.decompress(gpage).decode("gb2312")
		soup=BeautifulSoup(page,"lxml")
		date=soup.find_all("span",class_="s_f_l")[0].find_all("font")[1].string
		day=date.split(" ")[0]
		second=date.split(" ")[1]
		print("PROCESSING DATE "+day)
		pattern=re.compile(r"\d+-+\d+")
		for s in soup.find_all("div",class_="p_box")[0].find_all("div")[2].stripped_strings:
			result=re.findall(pattern,s)
			price=result[0].split("-")
			low=price[0]
			high=price[1]
			with open("data.txt","a+") as f:
				f.write(day+" "+second+" "+low+" "+high+"\n")
			break
		time.sleep(0.5)