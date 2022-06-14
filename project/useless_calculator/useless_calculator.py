# -*- coding = utf-8 -*-
# @Time : 2022/6/15 2:01
# @Author : 最帅杰尼龟(zsjng)
# @File : useless_calculator.py
# @Software : PyCharm

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print('b cannot be 0')
        else:
            return a / b

    def remainder(self, a, b):
        return a % b

    def pow(self, a, b):
        return a ** b

    def divisible(self, a, b):
        if b == 0:
            print('b cannot be 0')
        else:
            return a // b

    def batch_func(self, a_list, b_list, c):
        cal = {'add': self.add, 'sub': self.subtract, 'multiply': self.multiply,
               'divide': self.divide, 'remainder': self.remainder, 'pow': self.pow,
               'divisible': self.divisible}
        res_list = []
        for i in range(len(a_list)):
            res_list.append(cal[c](a_list[i], b_list[i]))
        return res_list


c = Calculator()
print(c.batch_func([3, 2, 1], [2, 3, 4], 'add'))
print(c.batch_func([3, 2, 1], [2, 3, 4], 'sub'))
