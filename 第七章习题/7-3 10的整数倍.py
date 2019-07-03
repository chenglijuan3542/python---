# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 7-3 10的整数倍.py
@time: 2019/7/1 14:34
@desc:
'''
num = input('Please input a number: ')
num = int(num)
if num % 10 ==0:
    print( str(num) + 'is times of 10.')
else:
    print(str(num) + 'is not times of 10.')