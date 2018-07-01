# -*- coding: utf-8 -*-
# @Time    : 2018/7/1 15:48
# @Author  : xuanle
# @FileName: osOrder.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import os
import time

cmd = input("please input your order：")
while cmd != "退出":

    time.sleep(1)#等待1s

    if cmd == "计算器":
        os.system("calc")

    elif cmd == "字符映射":
        os.system("charmap")

    elif cmd == "cmd":
        os.system("cmd.exe")

    elif cmd == "关机":
        os.system("Shutdown -s -t 600")

    elif cmd == "取消关机":
        os.system("shutdown -a ")

    elif cmd == "重启":
        os.system("Shutdown -r -t 600")

    elif cmd == "控制面板":
        os.system("control")

    elif cmd == "控制台":
        os.system("mmc")

    elif cmd == "远程连接":
        os.system("mstsc")

    elif cmd == "记事本":
        os.system("notepad")#同步打开，关闭前一个才会打开下一个

    elif cmd == "记事本异步":
        os.system("start notepad")#异步打开，连续打开无限个

    elif cmd == "屏幕键盘":
        os.system("osk")

    elif cmd == "进程":
        os.system("tasklist")

    else:
        print("no order")

    cmd = input("please input your order：")

else:
    os.system("exit()")
    print(" quite successful")
