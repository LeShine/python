# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 23:43
# @Author  : xuanle
# @FileName: win32circle.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import win32gui
import win32con
import math

QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
target = QQ
r = 300
while True:
    SE = 0.0
    while SE < 3.1415926535 * 2:
        x = int(r+r*math.cos(SE))
        y = int(r+r*math.sin(SE))
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, x, y, 400, 400, win32con.SWP_SHOWWINDOW)
        SE += 0.1
