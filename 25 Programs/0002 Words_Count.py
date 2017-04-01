#任一个英文的纯文本文件 统计其中的单词出现的个数

#Regular Expression

import re

def CountWords(file):
	with open(file) as f:
		text=f.read()
		words=re.findall(r"[a-zA-Z\-.]*[a-zA-Z]+",text)
		print(words)
		num=len(words)
	return num

file=input()
num=CountWords(file)
print(num)