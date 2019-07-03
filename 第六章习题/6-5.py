# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 6-5.py
@time: 2019/7/1 10:11
@desc:
'''
rivers = {'changjiang':'china','nile':'egypt','huanghe':'china'}
for river,country in rivers.items():
    print('The '+river.title() + ' runs through '+ country.title())
for river in rivers.keys():
    print('The rivers are: '+ river.title())
for country in rivers.values():
    print('The countrys are: '+ country.title())