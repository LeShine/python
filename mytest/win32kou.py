# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 23:09
# @Author  : xuanle
# @FileName: win32kou.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import win32con
import win32gui

notepad = win32gui.FindWindow("Notepad", "无标题 - 记事本")
QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")  # 找出qq窗体
target = QQ

while True:
    for x in range(800):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, x, 0, 400, 400, win32con.SWP_SHOWWINDOW)
    for x in range(800):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, 600, x, 400, 400, win32con.SWP_SHOWWINDOW)
    for x in range(800, 0, -1):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, x, 600, 400, 400, win32con.SWP_SHOWWINDOW)
    for x in range(800, 0, -1):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, 0, x, 400, 400, win32con.SWP_SHOWWINDOW)
    for x in range(800):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, 300, x, 400, 400, win32con.SWP_SHOWWINDOW)
    for x in range(800):
        win32gui.SetWindowPos(target, win32con.HWND_TOPMOST, x, 300, 400, 400, win32con.SWP_SHOWWINDOW)
