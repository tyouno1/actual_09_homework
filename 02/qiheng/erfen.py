#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s = [0,12,22,33,43,55,66,76,82,92]
print '数组内容为:%s' % s
num = raw_input('请输入数字:')
r = 0
h = len(s) - 1
i = 0

while r <= h:
	x = (r + h) / 2
	if s[x] == int(num):
		print '找到了:%s' % s[x]
		break
	elif s[x] > int(num):
		h = x - 1 
	elif s[x] < int(num):
		r = x + 1	
else:
	print '列表中没有你输入的数字'

