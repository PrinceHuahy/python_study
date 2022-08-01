# coding=utf-8
# @Time : 2022/8/1 9:36
# @Author : zsjng
# @File : main.py
# @Software : PyCharm

import pywinauto
from pywinauto import clipboard, Application
from pywinauto import keyboard
import pandas as pd
import io
import time

import psutil


def get_pid(process_name):
    pids = psutil.process_iter()
    for pid in pids:
        if (pid.name() == process_name):
            return pid.pid


app = Application().connect(process=get_pid('xiadan.exe'))
win = app.window(title_re='网上股票交易')
# win_tree = win.child_window(class_name = 'SysTreeView32')
# win_tree.get_item('\查询[F4]\资金股票').click()
handle = win.child_window(control_id=129, class_name='SysTreeView32')
# handle.get_item('\查询[F4]\资金股票').click()
#
# zijin = win.child_window(control_id=1016, class_name='Static').window_text()
# result = {
#             "可用余额": win.child_window(control_id=0x3F8,class_name='Static').window_text()
#         }
# print(result)
handle.get_item([0]).click()
# shizhi = win.child_window(control_id=1047, class_name='CVirtualGridCtrl')
# shizhi.set_focus()
# pywinauto.keyboard.SendKeys('^c')
# data = clipboard.GetData()
# df = pd.read_csv(io.StringIO(data), delimiter='\t', na_filter=False)
# df["股票市值"] = df["市值"].sum()
# print(df)
buy = win.child_window(control_id=1032, class_name="Edit")
buy.click()
stock_no = "600000"
buy.set_focus()
for i in range(len(stock_no)):
    pywinauto.keyboard.SendKeys(stock_no[i])
