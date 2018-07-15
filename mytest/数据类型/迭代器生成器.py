# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 15:37
# @Author  : xuanle
# @FileName: 迭代器生成器.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

# 迭代器  用于列表、集合、字典、tuple
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))  # 调用一次索引前进一次
for i in it:
    print(i)

# 列表生成式
mylist2 = [x for x in range(100) if x > 50]#中括号list
print(type(mylist2))

#列表生成器
mylist3 = (x for x in range(100) if x > 50)#小括号生成器
print(type(mylist3))
print(next(mylist3))
print(next(mylist3))
print(next(mylist3))
print(next(mylist3))

