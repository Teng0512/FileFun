"""
-*- coding utf-8 -*-
@Time    : 2023/12/28 10:31
@Author  : mila Administrator
@File    : aa.py
@Software: PyCharm
"""
import json

import yaml


json_path = r"F:\Download\code_edit\FileFun\src\json_to_yaml\a.json"
yaml_path = r"F:\Download\code_edit\FileFun\src\json_to_yaml\a.yaml"

with open(json_path, encoding="utf-8") as f:
    json_data = json.loads(f.read())

d = {
    "test_name":json_data['name']
}
d.update(json_data["allure"])
d["request"] = {}
for k,v in json_data["endpoint"].items():
    if v is None:
        continue
    if k in ["id", "name", "project"]:
        continue

    d["request"][k] = v

d["request"].update(json_data["api_args"])

d["extract"] = json_data["extract"]
d["validate"] = json_data["validate"]
print(d)

with open(yaml_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(d, f, allow_unicode=True)