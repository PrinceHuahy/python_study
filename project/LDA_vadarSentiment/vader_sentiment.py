# -*- coding = utf-8 -*-
# @Time : 2022/6/16 13:38
# @Author : 最帅杰尼龟(zsjng)
# @File : vader_sentiment.py
# @Software : PyCharm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
with open(r'result\top_list.txt', 'r') as f:
    top_list = f.readlines()
topic = []
for i in top_list:
    i = i.split('], [')
    for j in i:
        j = j.replace('[', '').replace(']', '').replace(r"'",'').replace(',','')
        sentences = j
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(sentences)
        print(str(vs))