"""
-*- coding utf-8 -*-
@Time    : 2024/1/24 10:54
@Author  : mila Administrator
@File    : selenium_options.py
@Software: PyCharm
"""
import pytest
from selenium.webdriver import Chrome, ChromeOptions
from common.settings import chrome_path
from selenium.webdriver.chrome.service import Service as ChromeService
options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable=automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=chrome_path)
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-site-isolation-trials')
options.add_argument('--lang=zh-CN')
options.add_argument('--window-size=1920,1080')
driver = Chrome(options=options,service=service)

driver.get('https://www.baidu.com')
driver.get_screenshot_as_file("page.png")

print(driver.title)
print("ok")

driver.quit()


@pytest.fixture(scope="class")
def chrome():
    from selenium.webdriver import Chrome, ChromeOptions
    from selenium.webdriver.chrome.service import Service as ChromeService
    from common.settings import chrome_path
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable=automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=chrome_path)
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-site-isolation-trials')
    options.add_argument('--lang=zh-CN')
    options.add_argument('--window-size=1920,1080')
    driver = Chrome(options=options,service=service)

    driver.get('https://www.baidu.com')
    driver.get_screenshot_as_file("page.png")


    print(driver.title)
    print("ok")

    yield driver

    driver.quit()

"""
代码分析：
这是一个使用Python的pytest框架和Selenium库编写的代码段，用于创建一个Chrome浏览器实例，并执行一些操作。以下是对代码的分析：

@pytest.fixture(scope="class")：这是一个pytest的fixture装饰器，它将在每个测试类之前运行一次。它的作用是创建一个Chrome浏览器实例，并在测试结束后关闭它。
from selenium.webdriver import Chrome, ChromeOptions：从selenium库中导入Chrome和ChromeOptions类。
from selenium.webdriver.chrome.service import Service as ChromeService：从selenium库中导入ChromeService类。
from commons.settings import chrome_path：从commons库的settings模块中导入chrome_path变量，这个变量应该包含Chrome浏览器的可执行文件的路径。
options = ChromeOptions()：创建一个ChromeOptions对象，用于配置Chrome浏览器的行为。
options.add_experimental_option("excludeSwitches", ["enable=automation"])：添加一个实验性选项，禁用Chrome的自动化检测。
options.add_experimental_option("useAutomationExtension", False)：添加一个实验性选项，禁用Chrome的自动化扩展。
service = ChromeService(executable_path=chrome_path)：创建一个ChromeService实例，并设置它的可执行文件路径为之前导入的chrome_path。
options.add_argument('--headless')：添加一个命令行参数，使Chrome浏览器在无头模式下运行，这意味着浏览器界面将不会显示。
options.add_argument('--no-sandbox')：添加一个命令行参数，禁用Chrome的沙盒机制。
options.add_argument('--disable-gpu')：添加一个命令行参数，禁用GPU。
options.add_argument('--disable-dev-shm-usage')：添加一个命令行参数，禁用devshm。
options.add_argument('--disable-site-isolation-trials')：添加一个命令行参数，禁用站点隔离试验。
options.add_argument('--lang=zh-CN')：添加一个命令行参数，设置语言为简体中文。
options.add_argument('--window-size=1920,1080')：添加一个命令行参数，设置浏览器窗口的大小为1920x1080。
driver = Chrome(options=options,service=service)：创建一个Chrome浏览器实例，并传入之前配置的选项和服务。
driver.get('https://www.baidu.com')：打开百度首页。
driver.get_screenshot_as_file("page.png")：将当前网页截图并保存为page.png文件。
print(driver.title)：打印当前网页的标题。
print("ok")：打印"ok"。
yield driver：yield driver将浏览器实例返回给pytest框架，以便在测试中使用。
driver.quit()：关闭浏览器实例。
这段代码的主要目的是创建一个配置了各种选项的Chrome浏览器实例，打开百度首页，截图当前页面并保存，然后返回这个浏览器实例以供测试使用。最后，它关闭浏览器实例以释放资源。
"""