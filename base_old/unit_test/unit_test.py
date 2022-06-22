# -*- coding = utf-8 -*-
# @Time : 2022/6/15 1:45
# @Author : 最帅杰尼龟(zsjng)
# @File : unit_test.py
# @Software : PyCharm

import unittest

"""
def my_div(a, b):
    return a / b


class TestFunc(unittest.TestCase):
    def test_div(self):
        self.assertEqual(my_div(2, 1), 2)
        self.assertEqual(my_div(2, -1), -2)
        self.assertEqual(my_div(2, 0), 1)


unittest.main()
"""


def my_func(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1


def my_func2(b):
    if b != 'yes':
        raise ValueError('you can only say yes!')
    else:
        return True


class TestFunc(unittest.TestCase):
    def test_func(self):
        self.assertEqual(my_func(1), 2)
        self.assertEqual(my_func(-1), 3)
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(my_func(i), 1)

    def test_func2(self):
        self.assertTrue(my_func2('yes'))
        with self.assertRaises(ValueError):
            my_func2('nononono')

unittest.main()
