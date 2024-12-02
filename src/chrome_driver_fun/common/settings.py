"""
@Filename:   commons/settings.py
@Author:      北凡
@Time:        2023/5/26 21:33
@Describe:    ...
"""
import os

from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 此文件不允许import 同项目的其他模块


driver_type = "chrome"
wait_max_time = 10
selenium_by = By.XPATH


test_case_path = ""
test_glob = "**/test_*.yaml"

extract_path = "extract.yaml"
rsa_pub_path = "api.pub"
chrome_path = os.path.join(BASE_DIR, "driver", "chrome_driver", "chromedriver.exe")
new_chrome_path = os.path.join(BASE_DIR, "driver", "chrome_new_path")
new_firefox_path = os.path.join(BASE_DIR, "driver", "firefox_new_path")
base_url = "http://47.107.116.139"


allure_epic = "码尚教育自动化测试系统"
allure_feature = "北凡默认模块"
allure_story = "北凡默认功能"
