# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 3-4567.py
@time: 2019/6/30 14:19
@desc:
'''
list = ['lisa','bob','justin','martin']
messages = 'I want to invite these persons '+list[0].title()+','+list[1].title()+' to attend my party.'
print(messages)
a = list.pop(1)
print(a.title()+' '+'was not attended.')
list.insert(1,'mary')
print(list)

list.insert(0,'tom')
list.insert(3,'jerry')
list.append('william')
print(list)
message1 = 'I found a bigger table and I want to invite  '+list[0].title(),list[3].title(),list[-1].title()
print(message1)
b='tom'
list.remove(b)
c=list.pop(1)
message2 = 'I just can invite '+ b.title()+' , '+c.title()+'.'
print(message2)# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 3-1 姓名.py
@time: 2019/6/30 13:46
@desc:
'''
names = ['lily','martin','justin','silly']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-1].title())
print(list)
del list[0]
print(list)
del list[1]
print(list)
