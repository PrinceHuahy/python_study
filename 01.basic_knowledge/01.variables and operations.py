# -*- coding = utf-8 -*-
# @Time : 2022/6/22 19:03
# @Author : 最帅杰尼龟(zsjng)
# @File : 01.variables and operations.py
# @Software : PyCharm

"""variables and operations"""

'''create variables'''
name = 'use quote to create a string variables.'
print(name)
name2 = "double quotes are ok."
print(name2)
name3 = '''
triple quotes can
make multiple lines string
just looks like this.
'''
print(name3)

name4,name5,name6 = 'name4','name5','name6'
print(name4,name5,name6)

name7 = name8 = name9 = 'we are same!'
print(name7,name8,name9)

'''print function'''
print('python are best!')
name = 'zsjng'
print(name + '\'s ' + 'python are best!')
print("Today " + 'is ' + "sunday" + '!')

'''math calculate'''
num_of_files = 10
print('My system have', num_of_files, 'files')

print('if I have 5 groups, each group have', num_of_files / 5, 'files')
# In python, division always return a float. don't be worry.
print('5 + 6 = ', 5 + 6)
print('5 - 2 = ', 5 - 2)
print('4 * 3 = ', 4 * 3)
print('9 / 3 = ', 9 / 3)
print('12 % 10 = ', 12 % 10)
print('5 ** 2 = ', 5 ** 2)
print('12 // 7 = ', 12 // 7)

# you can add string or string * int
print('a' + 'b' + 'c' + 'd' * 4)
a = 5
print('a = ',a)
a += 3
print('a += 3 -> a = ',a)
# just try -= *= /=


