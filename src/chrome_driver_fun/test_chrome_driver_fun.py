"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 10:19
@Author  : mila Administrator
@File    : test_chrome_driver_fun.py
@Software: PyCharm
"""
import pytest
from selenium.webdriver.common.by import By


class TestBaidu():

    def test_baidu_one(self, chrome):
        driver = chrome
        driver.maximize_window()
        driver.get("http://www.baidu.com")

    def test_baidu_two(self, chrome):
        driver = chrome
        driver.maximize_window()
        driver.get("http://www.baidu.com")
        a = driver.find_element(By.ID, "kw")
        print(a.text)