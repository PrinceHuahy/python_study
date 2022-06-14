# -*- coding = utf-8 -*-
# @Time : 2022/6/14 16:36
# @Author : 最帅杰尼龟(zsjng)
# @File : file_dir.py
# @Software : PyCharm
import os
import shutil  # be careful that it can delete all file in this dir!

print('current dir: ', os.getcwd())
print('list of dir: ', os.listdir())

# with exitst_ok = True. if you already have this dir it will still work.
os.makedirs('project', exist_ok=True)
print(os.path.exists('project'))

# if already have user just show the name, or create the dir

# user create
if os.path.exists('user/jng'):
    print('user exist')
else:
    os.makedirs('user/jng')
    print('user created')
print(os.listdir('user'))

# user cancel
if os.path.exists('user/jng'):
    shutil.rmtree('user/jng')  # be careful
    # os.removedirs('user/jng')
    print('user canceled')
else:
    print('user not exist')

# user rename
os.makedirs('user/jng', exist_ok=True)
# if zsjng is already exist well get an error.so should use try except or if
if os.path.exists('user/zsjng'):
    print('the name you want to change is already exist,please try again')
else:
    os.rename('user/jng', 'user/zsjng')
print(os.listdir('user'))

# show files
# 'w+' means if a.txt is not exist will create it.
with open('user/zsjng/a.txt', 'w') as f:
    f.write('nothing')
print(os.path.isfile('user/zsjng/a.txt'))  # True
print(os.path.exists('user/zsjng/a.txt'))  # True
print(os.path.isdir('user/zsjng/a.txt'))  # False
print(os.path.isdir('user/zsjng'))  # True


# rename file
def copy(path):
    # filename = os.path.basename(path)
    # dir_name = os.path.dirname(path)
    filename, dir_name = os.path.split(path)
    new_filename = 'new_' + filename
    return os.path.join(dir_name, new_filename)


print(copy('user/zsjng/a.txt'))
