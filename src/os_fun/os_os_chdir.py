"""
-*- coding utf-8 -*-
@Time    : 2023/12/23 10:06
@Author  : mila Administrator
@File    : os_os_chdir.py
@Software: PyCharm
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

path = r"G:\孔令刚——临时文件\2023study\20231124docker技术学习\docker入门到精通"

# 查看当前工作目录
retval = os.getcwd()
print("当前工作目录为 %s" % retval)

# 修改当前工作目录
os.chdir(path)

# 查看修改后的工作目录
retval = os.getcwd()

print("目录修改成功 %s" % retval)
