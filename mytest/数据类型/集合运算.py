# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 16:47
# @Author  : xuanle
# @FileName: 集合运算.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6, 7}

print(set1 - set2)#set1 有 set2 没有
print(set2 - set1)#set2 有 set1 没有
print(set1 | set2)#并集
print(set1 & set2)#交集
print(set1 ^ set2)#并集-交集


