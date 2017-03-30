#爬取Openjudge已通过题目
import urllib.request
import gzip
from bs4 import BeautifulSoup
pids=[]
num=0
#处理当前用户页
for i in range(5):
	pagen=i+1
	cpage=urllib.request.urlopen("http://openjudge.cn/user/752446/?page="+str(pagen)).read()
	soup=BeautifulSoup(cpage,"lxml")
	trs=soup.find_all("div",class_="user-group")[0].find("tbody").find_all("tr")
	#处理当前页每个题目
	for tr in trs:
		a_title=tr.find_all("td",class_="title")[0].find("a")
		a_result=tr.find_all("td",class_="result")[0].find("a")
		#对不重复的题目进行处理
		if a_title.string[:3] not in pids and a_result.string=='Accepted':
			num+=1
			print("PROCESSING PAGE "+str(pagen)+" NO."+str(num)+" CODE "+a_title.string)
			pids.append(a_title.string[:4])
			url=a_result['href']
			headers={
				"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Encoding":"gzip, deflate, sdch",
				"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
				"Cache-Control":"max-age=0",
				"Connection":"keep-alive",
				"Cookie":"PHPSESSID=6bosl1tilhr114cqhc8j6gvf17",
				"Host":"bailian.openjudge.cn",
				"Referer":"http://openjudge.cn/user/752446/",
				"Upgrade-Insecure-Requests":"1",
				"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
			}
			req=urllib.request.Request(url,headers=headers)
			page=urllib.request.urlopen(req).read()
			gpage=gzip.decompress(page)
			soupc=BeautifulSoup(gpage,"lxml")
			#保持pre代码格式并去掉标签
			code=str(soupc.find("pre"))[20:-6]
			#替换html字符实体
			code=code.replace("&nbsp;"," ")
			code=code.replace("&lt;","<")
			code=code.replace("&gt;",">")
			code=code.replace("&amp;","&")
			code=code.replace('&quot;','"')
			code=code.replace("&apos;","'")
			f=open("/Users/Aoi/Documents/Code/C&Cpp/Openjudge/"+a_title.string[:4]+" "+a_title.string[6:]+".cpp","wb+")
			f.write(code.encode("utf-8"))
			f.close()
