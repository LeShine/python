# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 17:46
# @Author  : xuanle
# @FileName: runscore.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import time


num, sum = 0, 0

# beginTime = time.time()
# while num < 100000000:
#     num += 1
#     sum += num
# endTime = time.time()
# print(endTime - beginTime)


beginTime = time.time()
for i in range(300000000):
    # num += 1
    sum += i
endTime = time.time()
print(endTime - beginTime)

