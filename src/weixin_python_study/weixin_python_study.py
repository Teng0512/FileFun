"""
-*- coding utf-8 -*-
@Time    : 2023/12/21 18:40
@Author  : mila Administrator
@File    : weixin_python_study.py
@Software: PyCharm
"""
from weixin import Weixin
#初始化 Weixin 对象
config = dict(WEIXIN_APP_ID="wx29e4b63eaff5af60",WEIXIN_APP_SECRET="2c0b65cebd523477df7eceaa0990eb22")
wx = Weixin(config)
access_token = wx.access_token(code="jdwdhasdjahsjd")
print(access_token)