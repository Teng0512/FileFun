"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 10:18
@Author  : mila Administrator
@File    : download_chrome_driver.py
@Software: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def download_chrome_driver():
    driver_path = ChromeDriverManager().install()
    service = ChromeService(executable_path=driver_path)
    print(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.quit()


if __name__ == '__main__':
    download_chrome_driver()
