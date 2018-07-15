# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 14:05
# @Author  : xuanle
# @FileName: set简介.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

myset = {1, 2, 3, 4, 5, 6}
myset.update([1, 2, 8, 9, 10])  # 去重
print(myset)
for i in myset:
    i += 2  # i是myset元素的副本，副本改变元素不会变，若要改变需将set转为list
    print(i)
# print(myset[0])    set 没有索引
for idx, iddata in enumerate(myset):  # enumerate 生成索引
    print(idx, iddata)  # idx:下标 iddata：值
# 类型转换
mylist = list(myset)
mytuple = tuple(myset)
print(mylist, mytuple)

# 常见方法
# myset.remove(100)#元素不存在，报错
myset.discard(100)  # 元素不存在，但不报错
myset.remove(10)
newset = myset.copy()  # 深复制
print(newset)
myset.pop()  # 弹出第一个元素
print(myset)
myset.clear()
print(myset)
print(newset)

# set运算符
set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6, 3, 4}
print(set1 - set2)
print(set2 - set1)
print(set2 & set1)  # 交集
print(set2 | set1)  # 去重合并
print(set2 ^ set1)  # 不一样的合并
print(1 in set1)  # True
print(set1 in set2)  # False  in & not in 只能用于元素与集合之间，不能用于集合与集合之间
print(set2.difference(set1))#独有的 5，6
print(set1.difference(set2))#独有的 空

#关系运算
print(set1>set2)#False 表示包含关系
print(set1<set2)#True
print(set2.issuperset(set1))#是否包含
print(set2.issubset(set1))#是否被包含

#不可变集合 frozenset  只能查看不能删除、增加、修改；set可增删
fz = frozenset([1,2,3,4])
print(fz)
print(type(fz))
for i in fz:
    print(i)







