# coding=utf-8
# @Time : 2022/7/27 23:04
# @Author : zsjng
# @File : main.py
# @Software : PyCharm

import easytrader

user = easytrader.use('ths')
user.connect(r'C:\同花顺软件\同花顺\xiadan.exe')
user.balance()