# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 7-5 电影票.py
@time: 2019/7/1 15:00
@desc:
'''
age = input('Your age is ')
age = int(age)
if age <= 3:
    print('free ticket')
elif age > 3 and age <= 12:
    print('You should pay 10 dollars')
else:
    print('You should pay 15 dollars')