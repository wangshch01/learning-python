#!/usr/bin/env python
#-*-coding:utf-8 -*-
str = input('请输入字符串:')

def func(str):
	a = list(str)
	b = len(a)
	for i in range(0,b):
		while i-1>=0:
			if a[i] > a[i-1]:
				return "Ture"
			else:
				return "False"
print func(str)
								
