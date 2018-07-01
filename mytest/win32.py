# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 22:25
# @Author  : xuanle
# @FileName: win32.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import win32con
import win32gui
import time

QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")  # 找出qq窗体

for i in range(10):
    time.sleep(1)
    if i % 2 == 0:
        win32gui.ShowWindow(QQ, win32con.SW_HIDE)  # 隐藏
    else:
        win32gui.ShowWindow(QQ, win32con.SW_SHOW)  # 展示
