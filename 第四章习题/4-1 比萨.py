# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 4-1 比萨.py
@time: 2019/6/30 16:29
@desc:
'''
pizzas = ['apple','liulian','pinapple']
friend_pizza = pizzas[:]
pizzas.append('pear')
friend_pizza.append('jiangguo')
for pizza in pizzas:
 print('My favorite pizzas are '+ pizza.title())
for pizza2 in friend_pizza:
 print('My friend favorite pizzas are '+ pizza2.title())
