# -*- coding = utf-8 -*-
# @Time : 2022/6/16 16:01
# @Author : 最帅杰尼龟(zsjng)
# @File : lda_test.py
# @Software : PyCharm

'''
1、先从爬取的内容中找出发布的内容，然后将其添加为数列
2、通过jieba对数据进行分类清洗
3、LDA通过词组获得主题
'''
import os
import re

import jieba
import jieba.posseg as psg
import numpy as np
import pandas as pd
import pyLDAvis
import pyLDAvis.sklearn

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

output_path = r'C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\result'
file_path = r'C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\data'
os.chdir(file_path)
data = pd.read_csv(r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\data\doc_ewujushi.csv")
os.chdir(output_path)
dic_file = r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\stop_dic\dict.txt"
stop_file = r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\stop_dic\stopwords.txt"


def chinese_word_cut(mytext):
    jieba.load_userdict(dic_file)  # 加载用户词典
    jieba.initialize()  # 手动初始化（可选）

    # 加载用户停用词表
    try:
        stopword_list = open(stop_file, encoding='utf-8')
    except:
        stopword_list = []
        print("error in stop_file")

    stop_list = []  # 存储用户停用词
    flag_list = ['n', 'nz', 'vn']  # 指定在jieba.posseg分词函数中只保存n：名词、nz：其他专名、vn：动名词
    for line in stopword_list:
        line = re.sub(u'\n|\\r', '', line)
        stop_list.append(line)

    word_list = []
    seg_list = psg.cut(mytext)  # jieba.posseg分词
    for seg_word in seg_list:
        word = re.sub(u'[^\u4e00-\u9fa5]', '', seg_word.word)  # 只匹配所有中文
        find = 0  # 标志位
        for stop_word in stop_list:
            if stop_word == word or len(word) < 2:  # 长度小于2或者在用户停用词表中，将被过滤
                find = 1
                break
        if find == 0 and seg_word.flag in flag_list:  # 标志位为0且是需要的词性则添加至word_list
            word_list.append(str(word))

    return (" ").join(word_list)


data["content_cutted"] = data.content.apply(chinese_word_cut)
# print(data)
'''
 Unnamed: 0  ...                                     content_cutted
0              0  ...  置顶 姐妹 内容 干货 网页 链接 小天地 男人 消费观 功课 调理 姨妈 朋友圈 经营 朋...      
1              1  ...
2              2  ...                        收款 银行 男帅 神仙 爱情 鳄鱼皮 跑车 大额 爱情
3              3  ...          粉丝 私信 脸皮 女生 礼物 淘宝 链接 发给 女生 块钱 眼部 女生 信息 全文
4              4  ...                                              联系 思念
...          ...  ...                                                ...
3723        3735  ...                                                 评论
3724        3736  ...                           平行 世界 伤心 人类 回收站 航德 金瓜 公子
3725        3737  ...                                              摸鱼 正事
3726        3738  ...                            野花 冲击 画面 厂长 图片 老刀 小豆 梓的
3727        3739  ...                                              话题 文案

'''

n_features = 1000  # 提取1000个特征词语
tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df=0.5,
                                min_df=10)
tf = tf_vectorizer.fit_transform(data.content_cutted)

n_topics = 7  # 手动指定分类数
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                learning_method='batch',
                                learning_offset=50,
                                doc_topic_prior=0.1,
                                topic_word_prior=0.01,
                                random_state=0)
lda.fit(tf)
n_top_words = 25
tf_feature_names = tf_vectorizer.get_feature_names()


def print_top_words(model, feature_names, n_top_words):
    tword = []
    save_topic = []
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        save_topic.append('!!!')
        save_topic.append(topic_idx)
        topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        tword.append(topic_w)
        print(topic_w)
        save_topic.append(topic_w)
    with open('topic_list.txt','w+',encoding='utf-8') as f:
        f.write(str(save_topic))
    return tword


topic_word = print_top_words(lda, tf_feature_names, n_top_words)

topics = lda.transform(tf)
topic = []
for t in topics:
    topic.append(list(t).index(np.max(t)))
data['topic'] = topic
data.to_excel("data_topic.xlsx", index=False)
print(topics[0])

# 启用下面两行可以生成可视化lda数据
# pic = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
# pyLDAvis.save_html(pic, 'lda_pass'+str(n_topics)+'.html')
