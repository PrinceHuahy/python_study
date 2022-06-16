# -*- coding = utf-8 -*-
# @Time : 2022/6/16 2:14
# @Author : 最帅杰尼龟(zsjng)
# @File : pandas_study.py
# @Software : PyCharm

"""
pandas_study
"""
import numpy as np
import pandas as pd

# import pandas as pd
# print(pd.Series([1,2,3]))


# df = pd.read_excel(r'data/体检数据.xlsx', index_col=0)
# print(df)
# df.loc[2, '体重'] = 1
# print(df)
# df.to_excel('data/体检数据_修改后.xlsx')

# with open('data/体检数据.csv', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# df = pd.read_csv('data/体检数据.csv', index_col=0,sep=',')
# print(df, type(df))

# df = pd.read_clipboard()
# print(df)

# df = pd.read_html("https://mofanpy.com/tutorials/data-manipulation/pandas/read-save/")
# print(df, type(df))

# l = [11, 22, 33]
# s = pd.Series(l)
# print('list:\n', l)
# print('series:\n', s)
# '''
# list:
#  [11, 22, 33]
# series:
#  0    11
# 1    22
# 2    33
# dtype: int64
# '''
# s1 = pd.Series(l, index=['a', 'b', 'c'])
# s2 = pd.Series({'d': 44, 'e': 55, 'f': 66})
# print(s1)
# print(s2)
# '''
# a    11
# b    22
# c    33
# dtype: int64
# d    44
# e    55
# f    66
# dtype: int64
#
# '''
# s3 = pd.Series(np.random.rand(3),index=['a', 'b', 'c'])
# print(s3)
# '''
# a    0.658733
# b    0.359269
# c    0.981606
# dtype: float64
# '''
# print('array:', s3.to_numpy())
# print('list:', s3.values.tolist())
# '''
# array: [0.65873268 0.35926862 0.9816063 ]
# list: [0.6587326774906086, 0.3592686225626113, 0.9816062989017192]
# '''
# df = pd.DataFrame([
#     [1,2],
#     [3,4]
# ])
# print(df)
# '''
#    0  1
# 0  1  2
# 1  3  4
# '''
# print(df.at[0,1])
# '''
# 2
# '''

# df = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
# # key -> col, value -> row.
# print(df)
# '''
#    col1  col2
# 0     1     2
# 1     3     4
# '''
# print(df['col1'],'\n')
# '''
# 0    1
# 1    3
# Name: col1, dtype: int64
# '''

# df = pd.DataFrame({'col1':pd.Series([1,3]),'col2':pd.Series([2,4])})
# print(df)
# '''
#    col1  col2
# 0     1     2
# 1     3     4
# '''

# s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
# df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
# print(s, "\n")
# print(df)
# '''
# a    1.0
# b    2.0
# c    3.0
# dtype: float64
#
#    col1  col2
# a     1     2
# b     3     4
# '''
#
# print(df.index, '\n')
# print(df.columns)
# '''
# Index(['a', 'b'], dtype='object')
#
# Index(['col1', 'col2'], dtype='object')
#
# '''
"""
choose data
"""

data = np.arange(-12, 12).reshape((6, 4))
'''
arange([start,] stop[, step,], dtype=None, *, like=None)
Return evenly spaced values within a given interval.
'''
df = pd.DataFrame(
    data,
    index=list('abcdef'),
    columns=list('ABCD')
)
# print(df)
# '''
#     A   B   C   D
# a -12 -11 -10  -9
# b  -8  -7  -6  -5
# c  -4  -3  -2  -1
# d   0   1   2   3
# e   4   5   6   7
# f   8   9  10  11
# '''
# print(df[['C', 'B']])
# '''
#     C   B
# a -10 -11
# b  -6  -7
# c  -2  -3
# d   2   1
# e   6   5
# f  10   9
# '''
# print('numpy:\n', data[:, [2,1]])
# '''
# numpy:
#  [[-10 -11]
#  [ -6  -7]
#  [ -2  -3]
#  [  2   1]
#  [  6   5]
#  [ 10   9]]
# '''
print(data[2:3, 1:3])
print(df.loc['c':'d','B':'D'])