#爬取Openjudge题目id及其通过人数
from bs4 import BeautifulSoup
import urllib.request
f=open("data.txt","w+")
for pn in range(24):
	page=urllib.request.urlopen("http://bailian.openjudge.cn/practice/?page="+str(pn+1)).read()
	soup=BeautifulSoup(page,"lxml")
	l=soup.find("tbody").find_all("tr")
	for tr in l:
		print(" Processing page "+str(pn+1)+" ID "+tr.find_all("td",class_="problem-id")[0].find("a").string+'\n')
		f.write(tr.find_all("td",class_="problem-id")[0].find("a").string+" ")
		f.write(tr.find_all("td",class_="accepted")[0].find("a").string+'\n')
f.close()
