"""
-*- coding utf-8 -*-
@Time    : 2024/1/1 11:42
@Author  : mila Administrator
@File    : win_toast_study.py
@Software: PyCharm
"""
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
header = input("请输入通知的类型：")
text = input("请输入要提示的信息：")
time_min = float(input("在几分钟内："))
i=1
for i in range(3):
    time_second = time_min * 60
    print("all set!")
    time.sleep(time_second)
    toaster.show_toast(f"{header}", f"{text}")
    i += 1
