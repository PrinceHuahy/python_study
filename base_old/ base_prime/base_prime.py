# -*- coding = utf-8 -*-
# @Time : 2022/6/15 17:04
# @Author : 最帅杰尼龟(zsjng)
# @File : base_prime.py
# @Software : PyCharm
"""
python prime function
"""

'''lambda'''

# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# add1 = lambda a, b: a + b
# print(add1(1, 2))

'''for-loop'''
# l = []
# for i in range(10):
#     l.append(i * 2)
# print(l)
# l1 = [i * 2 for i in range(10)]
# print(l1)
#
# d = {'index_' + str(i): i * 2 for i in range(10)}
# print(d)

'''if-else'''
# done = False
# if done:
#     a = 1
# else:
#     a = 2
# print(a)
#
# b = 1 if done else 2
# print(b)

'''for-if-loop'''
# l2 = [i * 2 for i in range(10) if i % 2 == 0]
# l3 = [i * 2 for i in range(10) if i % 2 == 1]
# print(l2)
# print(l3)

'''enumerate'''
# count = 0
# l = [11, 22, 33, 44]
# for data in l:
#     if count == 2:
#         data += 11
#     l[count] = data
#     count += 1
# print(l)
#
# h = [11, 22, 33, 44]
# for count, data in enumerate(h):
#     # use enumerate, it well be :
#     # 0,11   1,22  2,33  3,44
#     if count == 2:
#         data += 11
#     h[count] = data
# print(h)
#
# k = [11, 22, 33, 44]
# d = {}
# for count, data in enumerate(k, start=10):
#     d[count] = data
# print(d)
# # {10: 11, 11: 22, 12: 33, 13: 44}

'''zip'''

# name = ['a', 'b', 'c']
# score = [1, 2, 3]
# d = {}
# for i in range(3):
#     d[name[i]] = score[i]
# print(d)
#
# for j, k in zip(name, score):
#     d[j] = k
# print(d)
#
# bonus = [1, 0, 1]
# d1 = {}
# for i, j, k in zip(name, score, bonus):
#     d1[i] = j + k
# print(d1)

'''reverse & reversed'''
# l = [1,2,3]
# _l = []
# for i in range(len(l)):
#     _l.append(l[-i-1])
# print(_l)
# l.reverse()
# print(l)

'''copy & deepcopy'''
# l = [1,2,3]
# _l = l.copy()
# _l[0] = -1
# print(_l)
# print(l)
#
# l = [[1],[2],3]
# _l = l.copy()
# _l[0][0] = -1
# print(_l)
# print(l)
#
# class File:
#     def __init__(self,name):
#         self.name = name
#
# audio = File('mp3')
# file = File('txt')
# l = [audio,file]
# _l = l.copy()
# _l[0].name = 'mp4'
# print(audio.name)
#
# from copy import deepcopy
# l = [[1],[2],3]
# _l = deepcopy(l)
# _l[0][0] = -1
# print(_l)
# print(l)

'''generator'''
# items = []
# for item in range(5):
#     if item % 2 == 0:
#         items.append(item)
#
# for i in items:
#     print(i)
#
#
# def need_return():
#     for item in range(5):
#         if item % 2 == 0:
#             print(f'我要扔出一个{item}了')
#             yield item
#             print('我又回到里面了')
#
#
# for i in need_return():
#     print(i)
