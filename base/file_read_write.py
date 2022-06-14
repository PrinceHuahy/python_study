# -*- coding = utf-8 -*-
# @Time : 2022/6/14 16:09
# @Author : 最帅杰尼龟(zsjng)
# @File : file_read_write.py
# @Software : PyCharm
# f = open('new_file.txt','w')
# f.write('some text...')
# f.close()

# writelines with list. each element will write one line,should add \n
# with open('new_file2.txt','w') as f:
#     f.writelines(['some text for file2...\n','2nd line\n'])

# readlines will rad all txt into a list. each lines to be a list element
# with open('new_file2.txt','r') as f:
#     print(f.readlines())

# with open('new_file2.txt', 'r') as f:
#     while True:
#         line = f.readline()
#         line = line.replace('\n','')
#         print(line)
#         if not line:
#             break

# with open('chinese.txt','wb') as f:
#     f.write('这是中文的,this is Chinese'.encode('gbk'))
#
# with open('chinese.txt','r',encoding='gbk') as f:
#     print(f.read())

# with open('new_file.txt','r') as f:
#     print(f.read())
# with open('new_file.txt','r+') as f:
#     f.write('text has been replaced')
#     f.seek(0)  # seek(index) read with the line[index]
#     print(f.read())

with open("new_file.txt", "a+") as f:
    print(f.read())
    f.write("\nadd new line")
    f.seek(0, 0)  # 将开始读的位置从写入的最后位置调到开头
    print(f.read())
