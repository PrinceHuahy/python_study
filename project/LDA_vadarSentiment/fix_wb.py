# -*- coding = utf-8 -*-
# @Time : 2022/6/17 17:24
# @Author : 最帅杰尼龟(zsjng)
# @File : fix_wb.py
# @Software : PyCharm

import pandas as pd

df = pd.read_excel('wb3.xlsx')
# print(df.columns)
'''
Index(['用户ID', '用户名称', '性别', '介绍', '关注数', '粉丝数', '微博数', '地区或行业类别', '简介',
       '个性域名', '标签', '发布时间', '发布设备', '发布内容', '转发数', '评论数', '点赞数', '页面网址',
       '微博正文网址', '页码'],
      dtype='object')
'''
new_df = pd.concat([df['用户名称'].rename('author'), df['发布内容'].rename('content')], axis=1)
# axis = 0为上下合并，=1为左右合并
print(new_df)
new_df = new_df.dropna(subset=['content'])
new_df.to_csv('data\doc_ewujushi.csv', sep=',', index_label=None)


