"""
@Filename:   commons/settings.py
@Author:      北凡
@Time:        2023/5/26 21:33
@Describe:    ...
"""
import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))

chrome_path = os.path.join(BASE_DIR, "chrome_driver_fun", "driver", "chrome_driver", "chromedriver.exe")
print(chrome_path)
