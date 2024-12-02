"""
-*- coding utf-8 -*-
@Time    : 2023/12/31 11:44
@Author  : mila Administrator
@File    : thread_fun_one.py
@Software: PyCharm
"""
#  多线程示例
import time
from concurrent.futures.thread import ThreadPoolExecutor

test_path = [
    r"F:/Download/code_edit/Fu_CK/Cheng/Api_Requests/tests//beifan",
    r"F:/Download/code_edit/Fu_CK/Cheng/Api_Requests/tests//ddt",
]


def echo_http(path):
    print(time.time(), path)  # 替换成多进程启动测试框架


pool = ThreadPoolExecutor(max_workers=6)
pool.map(echo_http, test_path)