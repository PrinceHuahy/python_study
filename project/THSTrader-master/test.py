# -*- coding: utf-8 -*-
import pyautogui
from THS.THSTrader import THSTrader
import time

if __name__ == "__main__":
    trader = THSTrader(r"xiadan.exe")  # 连接客户端
    # 将网上股票交易系统移动到系统最右上角，然后显示在前台。如果出现任何不再提示的务必勾选。目前还差一个持有股票要跳验证码不好解决。
    # 如果显示器分辨率不是1920*1080的话。把主界面拖动到左上角然后显示完整后截屏给我。

    print(trader.get_balance())                            # 获取当前可用资金

    # print(trader.get_position())                           # 获取当前持有的股票
    # time.sleep(0.5)

    print(trader.buy(stock_no="600000", amount=100, price=7.08))  # 买入股票

    print(trader.sell(stock_no="600000", amount=100, price=7.08))  # 卖出股票
