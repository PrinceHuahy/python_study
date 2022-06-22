# -*- coding = utf-8 -*-
# @Time : 2022/6/22 19:02
# @Author : 最帅杰尼龟(zsjng)
# @File : 02.if_statement.py
# @Software : PyCharm

"""if statement"""

'''if'''
# if True:
#     print('It\'s True')
#
# if False:
#     print('It\'s False')
# if not False:
#     print('I am not False')
# # didn't see It's False? Because it's false, if statement will not run script
# # that after False.

'''if else'''
a, b = 3, 4
if a > b:
    print('a > b')
else:
    print('a < b')

print('-'* 40)
print(a > b and a > 0, a < b and b > 0, a >= b or a < b, not a <= b, a != b)
print('-'* 40)

if a > b and a > 0:
    print('a > b and a > 0')
elif a < b and b > 0:
    print('a < b and b > 0')
elif a >= b or a < b:
    print('a >= b or a < b')
else:
    print('a <= b')
# where is a >= b or a < b ? In if statement,if one is True, it will run script
# near ater the condition. And will not run another script. if all 'if' and 'elif'
# are False,it will run script after in 'else'.
if a >= b or a < b:
    print('a >= b or a < b')

today = '3'
if today == 1:
    print('Monday')
elif today == 2:
    print('Tuesday')
else:
    print('Today is not monday or tuesday')