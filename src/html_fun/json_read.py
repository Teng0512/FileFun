"""
-*- coding utf-8 -*-
@Time    : 2023/12/19 11:57
@Author  : mila Administrator
@File    : json_read.py
@Software: PyCharm
"""
import jsonpath
import json
with open("Bookmarks.json", encoding="utf-8") as fp:
    a = fp.read()
    b = json.loads(a)
c = b["roots"]["bookmark_bar"]["children"]
# print(c)
# print(len(c))
# print(c["children"][2]["children"][0]["date_added"])
# for i in c:
#     ss = c
print(len(c))

d = c[1]["children"]
for hh in d:
    # <DT><A HREF="https://www.baidu.com" ADD_DATE = "13325495550736634">good</A>
    print(f"<DT><A HREF= '{hh['url']}' ADD_DATE = '{hh['date_added']}'>{hh['name']}</A>")