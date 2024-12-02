"""
-*- coding utf-8 -*-
@Time    : 2023/12/29 10:18
@Author  : mila Administrator
@File    : download_chrome_driver.py
@Software: PyCharm
"""
import os
import shutil
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.settings import new_chrome_path,new_firefox_path


def download_chrome_driver():
    driver_path = ChromeDriverManager().install()
    service = ChromeService(executable_path=driver_path)
    print(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.quit()




def download_chromedriver():
    '''下载谷歌浏览器驱动'''
    download_driver_path = ChromeDriverManager().install()  # 使用ChromeDriverManager安装ChromeDriver，并获取驱动程序的路径
    shutil.copy(download_driver_path, new_chrome_path)  # 复制文件到目标位置
    print("自动安装driver的位置在：", download_driver_path)


def download_firfoxdriver():
    '''下载火狐浏览器驱动'''
    # folder_path = r'.\webdriver'  # 需要存放驱动文件的路径
    service = FireFoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.baidu.com")
    # download_driver_path = GeckoDriverManager().install()  # 下载FirefoxDriver
    # shutil.copy(download_driver_path, new_firefox_path)  # 复制文件到目标位置
    # print("自动安装driver的位置在：", download_driver_path)


def download_edgedriver():
    '''下载Edge浏览器驱动'''
    folder_path = r'.\webdriver'  # 需要存放驱动文件的路径
    download_driver_path = EdgeChromiumDriverManager().install()
    shutil.copy(download_driver_path, folder_path)  # 复制文件到目标位置
    print(download_driver_path)



if __name__ == '__main__':
    download_firfoxdriver()
