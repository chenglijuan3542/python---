# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 8-7.py
@time: 2019/7/3 10:36
@desc:
'''
def make_ablum(song_name,ablum_name,num = ''):
    describe_ablum= {'singer_name':song_name, 'ablum_name':ablum_name}
    if num:
        describe_ablum['num'] = num
    return describe_ablum
while True:
    print('\nPlease tell me your name: ')
    print("(enter 'q' at any time to quit)")

    song_name = raw_input("song_name:")
    if song_name == 'q':
        break

    ablum_name =raw_input("ablum_name:")
    if ablum_name == 'q':
        break
    ablum  = make_ablum(song_name,ablum_name)
    print(ablum)
