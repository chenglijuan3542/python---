# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 4-7 3的倍数.py
@time: 2019/6/30 17:09
@desc:
'''
list = []
for odd in range(3,31):
    if (odd % 3 == 0):
       list.append(odd)
print(list)