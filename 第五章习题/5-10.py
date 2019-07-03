# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 5-10.py
@time: 2019/7/1 9:38
@desc:
'''
current_users = ['1','2','3','admin','5']
new_users = ['1','admin','4','6','8']
for new_users in new_users:
    if new_users in current_users:
        print('we need a new user')
    else:
        print('this user name does not be used')