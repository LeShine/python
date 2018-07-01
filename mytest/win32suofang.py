# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 22:47
# @Author  : xuanle
# @FileName: win32suofang.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import win32con
import win32gui

notepad = win32gui.FindWindow("Notepad", "无标题 - 记事本")
# wangwang = win32gui.FindWindow("StandardFrame", "阿里旺旺")
for i in range(10):
    for size in range(0, 800, 1):
        win32gui.SetWindowPos(notepad,
                              win32con.HWND_TOPMOST,  #参考点==原点：左上角
                              size,  # 位置x
                              size,  # 位置y
                              size,  # 长度
                              size,  # 宽度
                              win32con.SWP_SHOWWINDOW)
    for size in range(800, 0, -1):
        win32gui.SetWindowPos(notepad,
                              win32con.HWND_TOPMOST,  #
                              size,  # 位置x
                              size,  # 位置y
                              size,  # 长度
                              size,  # 宽度
                              win32con.SWP_SHOWWINDOW)
