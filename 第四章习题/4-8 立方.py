# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 4-8 立方.py
@time: 2019/6/30 17:16
@desc:
'''
'''
list=[]
for value in range(1,11):
    trible = b=value**3
    list.append(trible)
print(list)
'''
list = [value**3 for value in range(1,11)]
print(list)
