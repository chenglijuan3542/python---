# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 5-8.py
@time: 2019/7/1 9:31
@desc:
'''
names = ['1','2','3','admin','5']
for name in names:
    if name == 'admin':
        print('Hello '+name +' ,would like to see a status report?')
    else:
        print('Hello ' + name +' , thank you for logging in again.')