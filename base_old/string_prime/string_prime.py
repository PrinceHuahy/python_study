# -*- coding = utf-8 -*-
# @Time : 2022/6/15 16:30
# @Author : 最帅杰尼龟(zsjng)
# @File : string_prime.py
# @Software : PyCharm

print('Hello,{0} {2} {1}'.format('Python', 'Script', '3.10.4'))

# name = 'zsjng'
# print('my name is ' + name + '!')
# print('my name is %s!' % name)

name = 'zsjng'
age = 18
gender = 'male'
# personal recommend f-string
# print('my name is ' + name + '! I am ' + str(age) + ' years old. I am a ' + gender)
# print('my name is %(name)s! I am %(age)d years old. I am a %(gender)s'
#       % {'name': name, 'age': age, 'gender': gender})
# print(f'my name is {name}! I am {age} years old. I am a {gender}')

age = 18000
# print(f'{age:,}')
# print(f'{age:b}')
# print(f'{age:d}')
# print(f'{age:f}')
# print(f'{age:.5f}')
# print(f'{age:%}')

str_test = '    i Have a PEN,I haVE An    apple.    '
print(str_test.strip())
print(str_test.replace('PEN','penpal'))
print(str_test.lower())
print(str_test.upper())
print(str_test.title())
print(str_test.split())
print('_'.join(str_test))
print(str_test.startswith(' '))
print(str_test.endswith('.'))

print(str_test.strip().title().replace('    ',' '))
"""
i Have a PEN,I haVE An    apple.
    i Have a penpal,I haVE An    apple.    
    i have a pen,i have an    apple.    
    I HAVE A PEN,I HAVE AN    APPLE.    
    I Have A Pen,I Have An    Apple.    
['i', 'Have', 'a', 'PEN,I', 'haVE', 'An', 'apple.']
 _ _ _ _i_ _H_a_v_e_ _a_ _P_E_N_,_I_ _h_a_V_E_ _A_n_ _ _ _ _a_p_p_l_e_._ _ _ _ 
True
False
I Have A Pen,I Have An Apple.

进程已结束,退出代码0

"""