# coding=utf-8
# @Time : 2022/7/13 19:57
# @Author : zsjng
# @File : spider.py
# @Software : PyCharm

import requests
from lxml import etree
import json
import csv


def save_messages(data, flag, path):
    global header
    if (flag == 1):
        header = ['小时', '温度', '风力方向', '风级', '降水量', '相对湿度', '空气质量']
    elif (flag == 2):
        header = ['日期', '天气', '最高温', '最低温', '风力', '风向']
    elif (flag == 3):
        header = []
    with open(path, 'w+', newline='') as fp:
        f_csv = csv.writer(fp)
        f_csv.writerow(header)
        for i in data:
            f_csv.writerow(i)
        print('信息存储完毕!')


def add_messages(data1, data2):
    header = ['日期', '天气', '最高温', '最低温', '风力', '风向']
    with open('西安未来十五天天气.csv', 'w', newline='') as fp:
        f_csv = csv.writer(fp)
        f_csv.writerow(header)
        for i in data1:
            f_csv.writerow(i)
        for i in data2:
            f_csv.writerow(i)
        print('信息存储完毕!')

    """
    xpath和python代码不同。不是以0开头p[1]代表第一个paragraph
    nodename选取此节点的所有子节点
    /从当前节点选取直接子节点
    //从当前节点选取子孙节点
    .选取当前节点
    ..选取当前节点的父节点
    @选取属性
    """
def obtain_sevenday_messages(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    tree = etree.HTML(response.text)
    all_li = tree.xpath('//ul[@class="t clearfix"]/li')
    messages = []
    for li in all_li:
        day = []
        day.append(li.xpath('./h1/text()')[0].split('日')[0])
        day.append(li.xpath('./p[1]/@title')[0])
        day.append(li.xpath('./p[2]/span/text() | ./p[2]/i/text()')[0].strip('℃'))
        day.append(li.xpath('./p[2]/i/text()')[0].strip('℃'))
        day.append(li.xpath('./p[3]/i/text()')[0])
        day.append(' '.join(li.xpath('./p[3]/em/span/@title')))
        messages.append(day)
    path = '西安七天天气.csv'
    save_messages(messages, 2, path)
    return messages


def obtain_fifteen_days_messages(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    tree = etree.HTML(response.text)
    all_li = tree.xpath('//ul[@class="t clearfix"]/li')
    messages = []
    for li in all_li:
        day = []
        s = li.xpath('./span/text()')
        day.append(s[0][3:5])
        day.append(s[1])
        day.append(li.xpath('./span[3]/em/text()')[0].strip('℃'))
        day.append(s[2].strip('℃').lstrip('/'))
        day.append(s[3])
        day.append(s[4])
        messages.append(day)
    path = '西安十五天天气信息.csv'
    save_messages(messages, 3, path)
    return messages


def get_the_new_of_the_day(url):
    one_day = []
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    tree = etree.HTML(response.text)
    all_div = tree.xpath('//div[@class="left-div"]')
    div = all_div[2]
    messages = div.xpath('string(./script)')
    messages = messages[messages.index('=') + 1:-2]
    jd = json.loads(messages)
    dayone = jd['od']['od2']
    for i in dayone:
        temp = []
        temp.append(i['od21'])  # 时间 ： 小时
        temp.append(i['od22'])  # 温度
        temp.append(i['od24'])  # 风向
        temp.append(i['od25'])  # 风级
        temp.append(i['od26'])  # 降水量
        temp.append(i['od27'])  # 相对湿度
        temp.append(i['od28'])  # 空气质量
        one_day.append(temp)
    path = '西安当天天气.csv'
    save_messages(one_day, 1, path)


def main():
    url = 'http://www.weather.com.cn/weather/101110101.shtml'
    url_2 = 'http://www.weather.com.cn/weather15d/101110101.shtml'
    data1 = obtain_sevenday_messages(url)
    data2 = obtain_fifteen_days_messages(url_2)
    get_the_new_of_the_day(url)
    add_messages(data1, data2)


if __name__ == "__main__":
    main()

