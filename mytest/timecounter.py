# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 17:59
# @Author  : xuanle
# @FileName: timecounter.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine


import os
import time

num = 0
while num < 100:
    time.sleep(1)
    num += 1
    # print("第" + str(num) + "秒")
    print("第", num, "秒")

    if num == 10:
        os.system("start notepad")#异步打开记事本
    if num == 20:
        os.system("taskkill /f /im notepad.exe")#关闭记事本进程
