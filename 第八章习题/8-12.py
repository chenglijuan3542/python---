# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 8-12.py
@time: 2019/7/3 15:14
@desc:
'''
def car(zhizaoshang,type,**car_info):
    car ={}
    car['zhizaoshang'] = zhizaoshang
    car['type'] = type
    for key,value in car_info.items():
        car[key] = value
    return car
make_car  = car('subaru','outback',color='blue',tow_package=True )
print(make_car)