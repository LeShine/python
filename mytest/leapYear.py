# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 18:02
# @Author  : xuanle
# @FileName: leapYear.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

year = eval(input("请输入年份："))
month = eval(input("请输入月份："))

if month == 1:
    print(31)
elif month == 2:
    if year % 100 != 0 and year % 4 == 0:
        print(29)
    elif year % 400 == 0:
        print(29)
    else:
        print(28)
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)
else:
    print("输入错误")
