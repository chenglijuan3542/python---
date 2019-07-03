# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 7-8 熟食店.py
@time: 2019/7/1 15:21
@desc:
'''
sandwich_orders = ['pork sandwich','pork sandwich','beef sandwich','pork sandwich']
finished_sandwiches = []
print('Our pork sandwiches are sold out.')
while  sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    while 'pork sandwich' in finished_sandwiches:
        finished_sandwiches.remove('pork sandwich')
print(finished_sandwiches)