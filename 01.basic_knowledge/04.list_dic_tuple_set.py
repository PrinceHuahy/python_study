# -*- coding = utf-8 -*-
# @Time : 2022/6/22 22:26
# @Author : 最帅杰尼龟(zsjng)
# @File : 04.list_dic_tuple_set.py
# @Software : PyCharm

"""list dictionary tuple set"""

'''list'''
files = ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt']
# index     0          1         2         3
# index     -4         -3        -2        -1
# both are right. files[1] == files[-3]. you can start with left or right.
for i in range(0, len(files)):
    print(files[i])
for file in files:
    print(file)

print(files[0])
files[0] = 'new_f1.txt'
print(files[0])

list_2 = ['you can put everything in list', 3.14, 5, True, False, [2, 3]]
print(list_2)
print(list_2[-1][1])
# list_2[-1] is [2,3]
# list_2[-1][1] is 3

'''dictionary'''

files = {'id': 111, 'passport': 'My passport', 'book': [1, 2, 3]}
print(files)
print(files['book'])
# dictionary = {key1:value1, key2:value2, key3:value3}
# dictionary[key1] -> value1

files['id'] = 333
print(files)
files['id'] = [1, 5, 6]
print(files)

'''tuple'''
# tuple look like list,but use () instead list[]. and you can not change element
a = [1, 2, 3]
files = ('file1', 'file2', 'file3', a)
print(files)
print(a)
a = [4, 5, 6]
print(files)
print(a)

'''set'''
# Each element in a set is unique,
# and the elements of a set are not ordered.

set_file = set(['file1', 'file2', 'file3'])
print(set_file)
# you can see set use {} but do not have key:value
set_file.add('file5')
print(set_file)
set_file.add('file4')
print(set_file)
set_file.remove('file1')
print(set_file)
print('-' * 40)
# each time you run those print. you can see element in set are unordered.

set_file2 = {'file1', 'file3', 'file4'}
print('intersection : ', set_file2.intersection(set_file))
print('union : ', set_file.union(set_file2))
print('difference : ', set_file.difference(set_file2))

'''work with loop'''

files = ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt']
for i in range(len(files)):
    if files[i] == 'f4.txt':
        print('I got f4.txt')
        break
    else:
        print(f'{files[i]} is not my target')
# let's make it easier.
for j in files:
    if j == 'f3.txt':
        print('I got f3.txt')
        break
# we can do this with dictionary too. values could be same.be careful
files = {'id': 111, 'passport': 'My passport', 'book': [1, 2, 3]}
for key, value in files.items():
    print(key, value)
for key in files.keys():
    print(files[key])
for value in files.values():
    print('values : ', files)

'''append pop'''

files = []
for i in range(5):
    files.append('f' + str(i) + '.txt')
    print(files)
for j in range(len(files) - 1):
    files.pop()
    print(files)
# looks beautiful right? look at under code.
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    print()

'''extend insert del remove'''
files = ['f1.txt', 'f2.txt']
extend_files = ['3.txt', '4.txt']
append_files = ['5.txt', '6.txt']
files.extend(extend_files)
print('extend : ', files, ' number of  elements : ', len(files))

files = ['f1.txt', 'f2.txt']

files.insert(1, 'file5.txt')
print('insert : ', files, ' number of  elements : ', len(files))
del files[1]
print(files)
files = ['f1.txt', 'f2.txt']
files.remove('f1.txt')
print(files)

'''get update'''

files = {"id": 111, "passport": "my passport", "books": [1, 2, 3]}
print('files["id"]:', files['id'])
print('files.get("id"):', files.get('id'))
print('files.get("id"):', files.get('Id'))
# if you are not sure the key is in dictionary, use d.get('possible key') will
# get a 'None' instead error!

files.update({'update_key': 'update_value'})
# update can add another dictionary's key:value into original dictionary.
print(files)
print('popped : ', files.pop('id'))
# in dictionary, pop must with a key,it will remove key:value
print('remain : ', files)
