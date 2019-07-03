# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 6-11.py
@time: 2019/7/1 10:40
@desc:
'''
cities = {
    'beijing':{
        'country':'china',
        'population':'10wan',
        'fact':'mountain people',
    },

    'paris':{
        'country':'france',
        'population':'1000000000',
        'fact':'so beautiful',
    },
}
for city,city_info in cities.items():
    print('\nCity: '+ city)
    population = city_info['population']
    fact = city_info['fact']
    print('\tPopulation: '+population)
    print('\tFact: '+fact)