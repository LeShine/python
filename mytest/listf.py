# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 23:42
# @Author  : xuanle
# @FileName: listf.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


myilst = [1,2,3,4,5]
myilst.append(8)
myilst.append(8)
print(myilst)
myilst.count(8)
print(myilst.index(8))#下标
print(myilst)
myilst.reverse()#反转
print(myilst)
myilst.sort()
print(myilst)
myilst.pop()#弹出最后一个
print(myilst)
# myilst.clear()#清空list
myilst.insert(1,22)#在下标1出插入22
myilst.remove(1)#删除1元素
print(myilst,id(myilst))
new = myilst.copy()
print(new,id(new))
print(myilst)








