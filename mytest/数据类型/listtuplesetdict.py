# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 22:57
# @Author  : xuanle
# @FileName: listtuplesetdict.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

mylist = [1, 2, 3, 4, 5, 6]  # 中括号
for data in mylist:
    print(data)

for i in range(len(mylist)):
    print(mylist[i])

mylist[5] = 10
print(mylist)  # list可修改元素值

print("-----list end------")
mytuple = (1, 2, 3, 4, 5, 6)  # 小括号
for data in mytuple:
    print(data)

for i in range(len(mytuple)):
    print(mytuple[i])

# mytuple[5] = 10 #tuple 不能修改元素值

print("----tuple end------")

myset = {1, 2, 3, 3}  # 大括号，元素不能重复,无序
print(myset)  # 123

for data in myset:
    print(data)

# for i in range(len(myset)):   #set 不支持index遍历
#     print(myset[i])

print("----set end------")

mydict = {"a": 1, "b": 2, "c": 3}  # 键重复无效，后者覆盖前者
print(mydict)

for key in mydict:
    print(mydict[key])

for data in mydict:
    print(data)  # 打印的是key

print("----dict end--------")

# 切片
print(mylist[:])  # mylist全部
print(mylist[2:])  # 第二个到结束
print(mylist[2:len(mylist)])  # 第二个到结束
print(mylist[2:-1])  # 第二个到最后一个不包含最后一个
print(mylist[:-1])  #
print(mylist[-len(mylist):-1])  #

print("----切片 end-------")

num = eval("12*2")  # eval:字符串转numb，包括表达式，只能操作字符串
print(num)

exec("print(\"hello world\")")  # exec:将文本当作命令执行，内部双引号需要加转义字符，或者外层用单引号

print(2 in mylist)#是否存在
print(20 not in mylist)#是否不存在

mylist2 = [x * x for x in range(10)]#列表构造表达式
print(mylist2)
