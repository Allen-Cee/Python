#使用 Python 生成 200 个激活码（或者优惠券）

#方案1 使用string和random模块
#方案2 使用uuid模块生成唯一标识符

import string
import random

#Coupon length
length=int(input())
char=string.ascii_uppercase+string.digits

def GenerateCoupon(length):
	c=''
	for i in range(length):
		c+=random.choice(char);
	return c

for i in range(200):
	print(GenerateCoupon(length));