"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 10:19
@Author  : mila Administrator
@File    : selenium_fun_1.py
@Software: PyCharm
"""

from selenium.webdriver.common.by import By


def get_by_fun():
    """获取By模块常用方法"""
    by_list = []
    for attr in dir(By):
        if attr.startswith("_"):
            continue
        by_list.append((attr,attr))

    print(by_list)
    return by_list


if __name__ == '__main__':
    get_by_fun()