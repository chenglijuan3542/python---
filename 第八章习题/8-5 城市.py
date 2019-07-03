# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 8-5 城市.py
@time: 2019/7/3 10:15
@desc:
'''
def describe_city(city_name,country='china'):
    print(city_name.title() + ' is in ' + country.title())
describe_city('beijing')
describe_city('tianjin')
describe_city('paris',country='france')