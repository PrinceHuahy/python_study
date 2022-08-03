# coding=utf-8
# @Time : 2022/8/4 1:11
# @Author : zsjng
# @File : main.py
# @Software : PyCharm

# 获取当前可用资金
# 获取当前持有的股票
# 买入股票
# 如果买入下单成功，尝试撤单
# 卖出股票

import pyautogui

# left-top is (0,0) right-bot is (1919 * 1079)
print(pyautogui.size())  # get screen size
print(pyautogui.position())  # get mouse location.
print(pyautogui.onScreen(100, 2000))  # return bool that location on screen or not.
'''mouse'''
# x, y = pyautogui.size()
# pyautogui.moveTo(x / 2, y / 2, duration=1)  # go to (x,y), duration: move time.
# pyautogui.moveRel(100, -200, duration=1)  # from now (x,y) go to (x+100,y-200)
# # pyautogui.click(x,y, **kw) clicks: click times. button: default left click.
# pyautogui.click(1137, 500, button='right', clicks=1, interval=0.2, duration=0.5)
# # pyautogui.scroll(times,x=None,y=None) # scroll mouse. can be negative
# pyautogui.scroll(-5, 1157, 500)
# # pyautogui.dragTo(x=None, y=None, duration=0.0, tween=linear, button=PRIMARY, logScreenshot=None, _pause=True,
# # mouseDownUp=True)
# pyautogui.dragTo(x / 2, y / x)  # hold button and move

'''Keyboard'''
# pyautogui.press('a')  # input 'a', can input Upper.
# pyautogui.click(1092, 417, duration=1)
# pyautogui.press(['h', 'e', 'l', 'l', 'o', 'w'], interval=5)
# str_lis = [x for x in 'hello, python!']
# pyautogui.typewrite(str_lis)
# pyautogui.typewrite('This is pyautogui!\n')
# CapsLock: typewrite(['capslock','a']) will get 'A'
# HotKeys
# pyautogui.hotkey('ctrl','shift','esc')