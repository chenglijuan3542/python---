# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 8-9.py
@time: 2019/7/3 12:51
@desc:
'''
def show_magicians(names):
    for name in names:
        print( name.title())

def make_great(names,names_change):
        while names:
            current_name = names.pop()
            current_names = "The Great " + current_name
            names_change.append(current_names)

names = ['zhangjie','xieman','suhvjbk']
names_change = []
make_great(names[:],names_change)   #副本
show_magicians(names)
show_magicians(names_change)
