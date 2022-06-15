# -*- coding = utf-8 -*-
# @Time : 2022/6/15 16:15
# @Author : 最帅杰尼龟(zsjng)
# @File : file_batch.py
# @Software : PyCharm

# 1st: look for all file
# 2nd: find special string
# 3rd: replace string

import os
import re
os.listdir('files')
for filename in os.listdir('files'):
    file_path = os.path.join(r'files',filename)
    with open(file_path,'r') as f:
        string = f.read()
        new_string = re.sub(r'morvanzhou.github.io','zsjng.github.io',string)
        with open(os.path.join('files','new_' + filename), 'w') as f2:
            f2.write(new_string)
