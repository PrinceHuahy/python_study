# coding=utf-8
# @Time : 2022/7/22 20:55
# @Author : zsjng
# @File : main.py
# @Software : PyCharm
import math

import pandas as pd
import numpy as np
import os
from math import log


# fix file
def main(filename):
    df = pd.read_csv(fr'SH600519\{filename}')  # import file
    df['BS'].replace(' ', np.nan, inplace=True)  # replace ' ' in BS column to Nan
    df.dropna(subset=['BS'], axis=0, how='any', inplace=True)  # drop BS column Nan row.
    df['tradeSign'] = df['BS'].astype(str).apply(create_tradesign).astype(float)  # create tradeSign

    l1 = find_corr(df, 'lag=1')
    l2 = find_corr(df, 'lag=2')
    l3 = find_corr(df, 'lag=3')
    y0 = 0
    y1 = log(find_corr(df, 'lag=1'))
    y2 = log(find_corr(df, 'lag=2'))
    y3 = log(find_corr(df, 'lag=3'))
    x = [1, 2, 3, 4]
    y = [y0, y1, y2, y3]

    w, b = find_slope(x, y)
    print(f'正在写入{filename}的结果')
    with open('ans.txt', 'a+') as f:
        f.write(f'{filename}\n')
        f.write(f'lag=1 corr = {l1}\n')
        f.write(f'lag=2 corr = {l2}\n')
        f.write(f'lag=3 corr = {l3}\n')
        f.write(f'rho = {math.e ** w}\n')
        f.write('=' * 50 + '\n')


def create_tradesign(x):
    if x == 'B':
        return '1'
    else:
        return '-1'


# print(df.info())
# df.to_csv('test.csv')

# lag=0   == 1

# df1 = pd.DataFrame()
# df1['lag=0'] = df['tradeSign']
# df1['tradeSign'] = df['tradeSign']
# print(df1.corr())

# lag=1
# df2 = pd.DataFrame()
# df2['tradeSign'] = df['tradeSign']
# df2['tradeSign'] = df2['tradeSign'].drop(index=df2['tradeSign'].index[0:1])  #
# df2['lag=1'] = df['tradeSign'].shift(axis=0, periods=1)  # diff lag1 down
# print(df2.corr())
#
#
# lag=2
# df3 = pd.DataFrame()
# df3['tradeSign'] = df['tradeSign']
# df3['tradeSign'] = df3['tradeSign'].drop(index=df3['tradeSign'].index[0:2])
# df3['lag=1'] = df['tradeSign'].shift(axis=0, periods=2)
# print(df3.info())
# print(df3.corr())


# lag=3


def find_corr(input_df, input_lag):
    x = 0
    if input_lag == 'lag=0':
        return 1
    elif input_lag == 'lag=1':
        x = 1
    elif input_lag == 'lag=2':
        x = 2
    elif input_lag == 'lag=3':
        x = 3
    df = pd.DataFrame()
    df['tradeSign'] = input_df['tradeSign']
    df['tradeSign'] = df['tradeSign'].drop(index=df['tradeSign'].index[0:x])
    df[f'lag={x}'] = input_df['tradeSign'].shift(axis=0, periods=x)
    # print(df['tradeSign'].head())
    # print(df[f'lag={x}'].head())
    str_corr = df.corr().to_string()
    return eval(str_corr.split(' ')[-3])


def find_slope(data_x, data_y):
    m = len(data_y)
    x_bar = np.mean(data_x)
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    for i in range(m):
        x = data_x[i]
        y = data_y[i]
        sum_yx += y * (x - x_bar)
        sum_x2 += x ** 2
    w = sum_yx / (sum_x2 - m * (x_bar ** 2))

    for i in range(m):
        x = data_x[i]
        y = data_y[i]
        sum_delta += (y - w * x)
    b = sum_delta / m
    return w, b


if __name__ == '__main__':
    dir_path = os.path.dirname(__file__)
    dir_lis = os.listdir(fr'{dir_path}/SH600519/')
    if 'ans.txt' in os.listdir():
        os.remove('ans.txt')
    for i in dir_lis:
        i.replace("'", '')
        main(i)
    print('写入完成')