# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 22:23
# @Author  : xuanle
# @FileName: strtemplate.py
# @Software: PyCharm
# @GitHub  ：https://github.com/LeShine

from string import Template

print(type(Template))
myste = Template("hello $name , 你好$a !")
print(myste.substitute(name = "xl",a = 'shuai'))





