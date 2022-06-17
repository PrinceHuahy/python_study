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

import numpy as np
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer

output_path = r'C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\result'
file_path = r'C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\data'
os.chdir(file_path)
data = pd.read_csv(r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\data\tweets_01-08-2021.csv")
os.chdir(output_path)
dic_file = r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\stop_dic\dict.txt"
stop_file = r"C:\Users\chen\PycharmProjects\python_study\project\LDA_vadarSentiment\stop_dic\stopwords.txt"

# print(data.columns)
'''
Index(['id', 'text', 'isRetweet', 'isDeleted', 'device', 'favorites',
       'retweets', 'date', 'isFlagged'],
      dtype='object')
'''
# print(data['text'][0])



document_column_name = '回答内容'
pattern = re.compile(r'\d|\W|_')

df = data
df = df.drop_duplicates()
df = df.dropna()
df = df.rename(columns={
    document_column_name: 'text'
})
df['cut'] = df['text'].apply(lambda x: str(x))
df['cut'] = df['cut'].apply(lambda x: re.sub(pattern, ' ', x))
# print(df['cut'])

tf_idf_vectorizer = TfidfVectorizer()
tf_idf = tf_idf_vectorizer.fit_transform(df['cut'])

feature_names = tf_idf_vectorizer.get_feature_names()
# 特征词 TF-IDF 矩阵
matrix = tf_idf.toarray()
feature_names_df = pd.DataFrame(matrix, columns=feature_names)
# print(feature_names_df)

n_topics = 7
lda = LatentDirichletAllocation(
    n_components=n_topics, max_iter=50,
    learning_method='online',
    learning_offset=50.,
    random_state=0)
lda.fit(tf_idf)


def top_words_data_frame(model: LatentDirichletAllocation,
                         tf_idf_vectorizer: TfidfVectorizer,
                         n_top_words: int) -> pd.DataFrame:

    rows = []
    feature_names = tf_idf_vectorizer.get_feature_names()
    for topic in model.components_:
        top_words = [feature_names[i]
                     for i in topic.argsort()[:-n_top_words - 1:-1]]
        rows.append(top_words)
        with open('top_list.txt','w+',encoding='utf-8') as f:
            f.write(str(rows))
            f.write('\n')
    columns = [f'topic {i + 1}' for i in range(n_top_words)]
    df = pd.DataFrame(rows, columns=columns)

    return df
if os.path.exists(r'result\top_list.txt'):
    os.remove(r'result\top_list.txt')
top_words_df = top_words_data_frame(lda, tf_idf_vectorizer, 20)
top_words_df.to_csv('top_words.csv', encoding='utf-8', index=None)



