1# -*- coding:utf-8 -*-
'''
@author: Kevin_lzj
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: kevin_lzj2018@google.com
@file: 4-3.py
@time: 2019/6/30 16:48
@desc:
'''
import time
start = time.time()
nums = []
for i in range(1,1001):
    nums.append(i)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
end = time.time()
print(end-start)
