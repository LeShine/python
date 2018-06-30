# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 23:49
# @Author  : xuanle
# @FileName: whilefloat.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import random

roundN = random.randint(1, 100)
print("输了" if roundN < 80 else "赢了")

# money = 2.0
# while money > 1e-10:
#     money -= 0.1
#     print(money)
#
#
# while money != 0:             #死循环：浮点误差
#     money -= 0.1
#     print(money)
#
