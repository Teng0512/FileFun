"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 10:19
@Author  : mila Administrator
@File    : test_chrome_driver_fun.py
@Software: PyCharm
"""
import pytest
from selenium.webdriver.common.by import By
from time import sleep


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

    def test_ces_one(self, chrome):
        driver = chrome
        driver.maximize_window()
        driver.get("https://52ce.com/tcping/")
        a = driver.find_element(By.XPATH, "//a[contains(text(),'首页')]")
        a.click()

    def test_ces_two(self, chrome):
        driver = chrome
        driver.maximize_window()
        driver.get("https://52ce.com/tcping/")
        do_type = '首页'
        if do_type in ['首页','在线Ping']:
            elements = driver.find_elements(by=By.XPATH, value=f"//a[contains(text(),'{do_type}')]")
            for temp in elements:
                temp.click()
                sleep(2)

    def test_ces_three(self, chrome):
        driver = chrome
        driver.maximize_window()
        driver.get("https://52ce.com/tcping/")
        do_type = '首页'
        temp = driver.find_element(by=By.XPATH, value=f"//a[contains(text(),'{do_type}')]")
        temp.click()
        do_type = '在线Ping'
        temp = driver.find_element(by=By.XPATH, value=f"//a[contains(text(),'{do_type}')]")
        temp.click()