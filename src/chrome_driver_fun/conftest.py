"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 15:20
@Author  : mila Administrator
@File    : conftest.py
@Software: PyCharm
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from .settings import *


@pytest.fixture(scope="class")
def chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable=automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=chrome_path)
    chrome_driver = webdriver.Chrome(service=service, options=options)
    return chrome_driver
