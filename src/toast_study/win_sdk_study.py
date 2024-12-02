"""
-*- coding utf-8 -*-
@Time    : 2024/1/1 11:54
@Author  : mila Administrator
@File    : win_sdk_study.py
@Software: PyCharm
"""
import winsdk.windows.ui.notifications as notifications
from winsdk.windows.data.xml.dom import XmlDocument, XmlNodeList
def notifier(message) -> None:
    notif_manager = notifications.ToastNotificationManager
    toast_xml: XmlDocument = notif_manager.get_template_content(
        notifications.ToastTemplateType.TOAST_TEXT02)
    toast_text_elements: XmlNodeList = toast_xml.get_elements_by_tag_name(
        "text")
    toast_text_elements[0].append_child(
        toast_xml.create_text_node("title"))
    toast_text_elements[1].append_child(toast_xml.create_text_node(message))
    toast = notifications.ToastNotification(toast_xml)
    notif_manager.create_toast_notifier("Python").show(toast)



if __name__ == '__main__':
    notifier("hello world")