# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 14:59
# @Author  : xuanle
# @FileName: dict简介.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

mydict = {"abcdefg": 10, "123456": 55, "123456": 555}
print(mydict)
print(mydict["abcdefg"])
for key in mydict:  # key
    print(mydict[key])

print("-------------")
for k in mydict.items():  # key:value的映射
    print(k)

# 字典的更新
password = '123456'
if password in mydict:
    mydict[password] += 1
else:
    mydict[password] = 1

print(mydict)

#字典删除
del mydict[password]
print(mydict)
print("----------------")


# print(mydict['123456'])#找不到报错
print(mydict.get("123456"))#找不到不报错
print("-----------------------")
print(mydict.items())
print(mydict.keys())
print(mydict.values())
mydict2 = {"ddd":222}
mydict.update(mydict2)#拼接
print(mydict,mydict2)

mydict2.setdefault("123456",None)
print(mydict2["123456"])















