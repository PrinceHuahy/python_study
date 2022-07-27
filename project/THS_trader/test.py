# -*- coding: utf-8 -*-

from THS.THSTrader import THSTrader
import time

# if __name__ == "__main__":
    # trader = THSTrader(r"C:\同花顺软件\同花顺\xiadan.exe")    # 连接客户端
    #
    # print(trader.get_balance())                            # 获取当前可用资金
    #
    # print(trader.get_position())                           # 获取当前持有的股票
    #
    # print(trader.sell(stock_no="162411", amount=100, price=0.238))  # 卖出股票
    #
    # result = trader.buy(stock_no="162411", amount=100, price=0.218)  # 买入股票
    # print(result)
    # time.sleep(5)
    # if result["success"] == True:						   # 如果买入下单成功，尝试撤单
    #     print("撤单测试--->", end="")
    #     print(trader.cancel_entrust(entrust_no=result["entrust_no"]))

    # -*- coding: utf-8 -*-
import pywinauto
import time
from pywinauto import application


class AccessDeniedError(Exception):
    """Raise when current user is not an administrator."""
    def __init__(self, arg):
        self.args = arg

class NoExistGroupError(Exception):
    """Raise when group Administrators is not exist."""
    def __init__(self, arg):
        self.args = arg


exe_path = r"C:\同花顺软件\同花顺\xiadan.exe"
print("正在连接客户端:", exe_path, "......")

# app = pywinauto.Application().connect(path=r'C:\同花顺软件\同花顺\xiadan.exe', timeout=10)
app = pywinauto.Application().connect(title_re='网上股票交易系统5.0')
print("连接成功!!!")
if r"网上股票" not in app.top_window().window_text():
    app.top_window().set_focus()
    pywinauto.keyboard.SendKeys("{ENTER}")
    print("设置下单软件为第一界面,handle= ", hex(app.top_window().handle), "text = ", app.top_window().is_dialog())

# app.window(title=u"网上股票交易系统5.0").print_control_identifiers()

# app.window(title=u"网上股票交易系统5.0").window(best_match='#32770').print_control_identifiers()
app.window(title=u"网上股票交易系统5.0").window(control_id=129, class_name='SysTreeView32').print_control_identifiers()
tree = app.window(title=u"网上股票交易系统5.0").hexin_scroll_wnd2.tree_view
groups = tree.get_item(r'\市价委托\买入')
groups.click()
