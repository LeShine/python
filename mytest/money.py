# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 20:48
# @Author  : xuanle
# @FileName: money.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

money = input("请输入金额")
yuan = int(eval(money))
jiao = int(eval(money) * 10) % 10
fen = (round(eval(money) * 100)) % 10
print(round(eval(money), 2))
print((round(eval(money) * 100)) % 10)
print(yuan, "元",
      jiao, "角",
      fen, "分"
      )
