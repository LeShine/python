# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 23:02
# @Author  : xuanle
# @FileName: voice.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("你太帅了")


