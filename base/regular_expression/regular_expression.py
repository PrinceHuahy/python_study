# -*- coding = utf-8 -*-
# @Time : 2022/6/14 19:50
# @Author : 最帅杰尼龟(zsjng)
# @File : regular_expression.py
# @Software : PyCharm

import re

"""
ptn = re.compile(r'\w+?@\w+?\.com')

matched = ptn.search('jng@zsjng.com')

print('jng@zsjng.com is a valid email:\n', matched)
matched = ptn.search('jng@zsjng+com')
print('jng@zsjng.com is a valid email:\n', matched)

print(re.search(ptn,'the email is jng@zsjng.com.'))

match = re.search(r'run', 'I run to you')
print(match)
# group will return the str in match
print(match.group())
# ( ab|adc )means  ab or adc.
print(re.search(r'(ran|run)', 'I ran to you'))
#  [xy] means x or y
print(re.search(r'r[au]n', 'I run to you'))
"""
#
"""
regular_expression:
\d    : [0-9]
\D    : not \d  # upper alpha means not lower alpha
\s    : [\t \n \r \f \v]
\S    :
\w    : [0-9a-zA-Z_]
\W    :
\b    : boundary . eg: 'er' in 'never' get 'er' , 'verb' not get 'er'
\B    :
\\    : compile '\'
.     : compile anything but '\n'
?     : previous mode is optional
*     : repeat zero or more times
+     : 1 or more times
{n,m} : repeat n times to m times
{n}   : repeat n times
+?    : find the minimum compile with +
*?    : find the minimum compile with *
??    : find the minimum compile with ?
^     : find line start. will find every line with re.M
$     : find line end. will find every line with re.M
\A    : find txt start
\B    : find txt end
"""
# re use
"""
# re.search()  # search all string and return the first one matched.
print(re.search(r'run', 'i run to you'))
# <re.Match object; span=(2, 5), match='run'>

# re.match()  # just search the first string. 
# eg: re.match(r'run','I run to you') is None
print(re.match(r'run', 'I run to you'))
# None

# re.findall()  # return a list than all matched each only one.
print(re.findall(r'r[ua]n', 'I run to you. you ran to him'))
# ['run', 'ran']

# re.finditer()  # look like below
for item in re.finditer(r'r[ua]n', 'I run to you. you ran to him'):
    print(item)
    # <re.Match object; span=(2, 5), match='run'>
    # <re.Match object; span=(18, 21), match='ran'>

# re.split()  # use re to split string,just like split('str')
print(re.split(r'r[ua]n', 'I run to you. you ran to him'))
# ['I ', ' to you. you ', ' to him']

# re.sub()  # use re to replace string.
print(re.sub('r[au]n','fly','I run to you. you ran to him'))
# I fly to you. you fly to him

# re.subn()  # same as re.sub but return a number show how many replace times
print(re.subn('r[au]n','fly','I run to you. you ran to him'))
# ('I fly to you. you fly to him', 2)
"""
#
"""
found = []
# r'[\w-]+?' means at least one time with \w-
# \.jpg means end with .jpg
str = 'I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg'
for i in re.finditer(r'[\w-]+?\.jpg', str):
    # group means the string in match= "string"
    found.append(re.sub(r'.jpg', '', i.group()))
print(found)
# ['2021-02-01', '2021-02-02', '2021-02-03']

# we can use () in r'[\w-]+?\.jpg like r'([\w-]+?)\.jpg that we only get
# return in ().
print(re.findall(r'([\w-]+?)\.jpg', str))
# ['2021-02-01', '2021-02-02', '2021-02-03']
# you can find the answer are same .amazing!
match = re.finditer(r'(\d+?)-(\d+?)-(\d+?)\.jpg', str)
for i in match:
    print("matched string:", i.group(0), ",year:",
          i.group(1), ", month:", i.group(2), ", day:", i.group(3))
print('-' * 80)
match = re.finditer(r'(\d+?)-(\d+?)-(\d+?)\.jpg', str)
for j in match:
    print("year:", j[0], ", month:", j[1], ", day:", j[2])

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
print('-' * 80)
match = re.finditer(r"(?P<y>\d+?)-(?P<m>\d+?)-(?P<d>\d+?)\.jpg", string)
# (?P<name>...) The substring matched by the group is accessible by name.
for file in match:
    print("matched string:", file.group(0),
          ", year:", file.group("y"),
          ", month:", file.group("m"),
          ", day:", file.group("d"))
"""

ptn, string = r"r[ua]n", "I Ran to you"
print("without re.I:", re.search(ptn, string))
print("with re.I:", re.search(ptn, string, flags=re.I))

ptn = r'^ran'
str = '''I
ran to you'''
print(re.search(ptn,str,flags=re.M))
# re.S can get \n