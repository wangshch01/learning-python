#!/usr/bin/env python
#-*-coding:utf-8 -*-
str = input('请输入字符串:')

def func(str):
	for x in range(len(str)):
		if x == len(str) - 1:
			return True
		elif str[x] >= str[x+1]:
			return False
print func(str)

##假设 len(str)为7,该函数判断的是当前位和下一位的大小，判断到data[6]的时候其实也就已经判断完了,当判断到data[6]的时候，说明前面都没有问题，这时候返回True即可.如果前面有问题，肯定早就返回False了.
