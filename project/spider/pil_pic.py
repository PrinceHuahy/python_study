# coding=utf-8
# @Time : 2022/7/13 19:59
# @Author : zsjng
# @File : pil_pic.py
# @Software : PyCharm
import pandas as pd
import math
from matplotlib import pyplot as plt


def tem_chart_of_the_fifteenth(data):  # 绘制未来十五天温度变化图
    date = list(data['日期'])
    tem_low = list(data['最低温'])
    tem_high = list(data['最高温'])
    for i in range(0, 15):
        if math.isnan(tem_low[i]):
            tem_low[i] = tem_low[i - 1]
        if math.isnan(tem_high[i]):
            tem_high[i] = tem_high[i - 1]
    tem_high_avg = sum(tem_high) / len(tem_high)
    tem_low_avg = sum(tem_low) / len(tem_low)
    tem_max = max(tem_high)
    tem_min = min(tem_low)
    tem_max_data = tem_high.index(tem_max)
    tem_min_data = tem_low.index(tem_min)
    x = range(1, 16)
    plt.figure(1, figsize=(20, 10))
    plt.plot(x, tem_high, color='r', label='高温')  # 绘制高温曲线
    plt.scatter(x, tem_high, color='r')
    plt.plot(x, tem_low, color='blue', label='低温')  # 绘制低温曲线
    plt.scatter(x, tem_low, color='blue')
    plt.plot([1, 16], [tem_high_avg, tem_high_avg], c='black', linestyle='--', label='平均高温')
    plt.plot([1, 16], [tem_low_avg, tem_low_avg], c='black', linestyle='--', label='平均低温')
    plt.legend()
    plt.text(tem_max_data + 1.15, tem_max + 0.15, str(tem_max), ha='center', va='bottom', fontsize=10.5)  # 标记出最高值
    plt.text(tem_min_data + 1.15, tem_min + 0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)  # 标记出最低值
    plt.xticks(x)
    plt.title('未来十五天温度变化图')
    plt.xlabel('天数/天')
    plt.ylabel('摄氏度/℃')
    plt.show()


def fifteenday_weather_map(data):  # 绘制天气饼状图
    colors = ["#F96900", "#F1EA0C", "#90F10C", "#0CF1CB", "#C00CF1", "#F10C7E"]
    date = list(data['日期'])
    weather = list(data['天气'])
    weather_num = []
    weather_set = []
    for i in weather:
        if i not in weather_set:
            weather_set.append(i)
    for i in weather_set:
        num = weather.count(i)
        weather_num.append(num)
    plt.figure(1, figsize=(12, 12))
    plt.pie(weather_num, labels=weather_set, startangle=60, colors=colors, autopct="%3.1f%%")
    plt.title('未来十五天天气分布图')
    plt.legend()
    plt.show()


def weayher_chart_of_the_day(data):  # 绘制当天温度变化图
    x = [i for i in range(24)]
    y = []
    hour = list(data['小时'])
    tem = list(data['温度'])
    for i in range(len(tem)):
        if math.isnan(tem[i]) == True:
            tem[i] = tem[i + 1]
    tem_avg = sum(tem) / len(tem)
    tem_high = max(tem)
    tem_min = min(tem)
    tem_max_hour = hour[tem.index(tem_high)]
    tem_min_hour = hour[tem.index(tem_min)]
    tem_min_data = tem.index(tem_min)

    for i in range(24):
        y.append(tem[hour.index(i)])
    plt.figure(1, figsize=(20, 10))
    plt.plot(x, y, color='red', label='温度')
    plt.scatter(x, y, color='red')
    plt.plot([1, len(tem)], [tem_avg, tem_avg], color='black', linestyle='--', label='平均相对气温')
    plt.legend()
    plt.text(tem_max_hour + 0.15, tem_high + 0.15, str(tem_high), ha='center', va='bottom', fontsize=10.5)  # 标记出最高值
    plt.text(tem_min_hour + 0.15, tem_min + 0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)
    plt.xticks(x)
    plt.title('当天气温变化图')
    plt.xlabel('时间/小时')
    plt.ylabel('摄氏度/℃')
    plt.show()


def daily_relative_humidity(data):  # 绘制当天相对湿度变化图
    x = [i for i in range(24)]
    y = []
    hour = list(data['小时'])
    humidness = list(data['相对湿度'])
    for i in range(len(humidness)):
        if math.isnan(humidness[i]):
            humidness[i] = humidness[i + 1]
    humidness_avg = sum(humidness) / len(humidness)
    humidness_max = max(humidness)
    humidness_min = min(humidness)
    humidness_max_hour = hour[humidness.index(humidness_max)]
    humidness_min_hour = hour[humidness.index(humidness_min)]
    for i in range(24):
        y.append(humidness[hour.index(i)])
    plt.figure(1, figsize=(20, 10))
    plt.plot(x, y, color='blue', label='湿度')
    plt.scatter(x, y, color='blue')
    plt.plot([1, len(humidness)], [humidness_avg, humidness_avg], color='black', linestyle='--', label='平均相对湿度')
    plt.legend()
    plt.text(humidness_max_hour + 0.15, humidness_max + 0.15, str(humidness_max), ha='center', va='bottom',
             fontsize=10.5)  # 标记出最高值
    plt.text(humidness_min_hour + 0.15, humidness_min + 0.15, str(humidness_min), ha='center', va='bottom',
             fontsize=10.5)
    plt.title('一天相对湿度变化图')
    plt.xticks(x)
    plt.xlabel('时间/小时')
    plt.ylabel('相对湿度/％')
    plt.show()


def air_quality_chart_of_the_day(data):  # 绘制当天空气质量变化图
    x = [i for i in range(24)]
    y = []
    hour = list(data['小时'])
    air = list(data['空气质量'])
    for i in range(len(air)):
        if math.isnan(air[i]):
            air[i] = air[i + 1]
    air_avg = sum(air) / len(air)
    air_max = max(air)
    air_min = min(air)
    air_max_hour = hour[air.index(air_max)]
    air_min_hour = hour[air.index(air_min)]
    for i in range(24):
        y.append(air[hour.index(i)])
    plt.figure(1, figsize=(10, 10))
    plt.bar(x, y, color='blue', label='空气质量')
    plt.plot([1, len(air)], [air_avg, air_avg], color='black', linestyle='--', label='平均空气质量')  # 添加平均线
    plt.legend()  # 显示设置好的标签
    plt.text(air_max_hour + 0.15, air_max + 0.15, str(air_max), ha='center', va='bottom', fontsize=10.5)  # 标记出最高值
    plt.text(air_min_hour, air_min + 0.20, str(air_min), ha='center', va='bottom', fontsize=10.5)  # 标记处最低值
    plt.title('当天空气质量变化图')
    plt.xticks(x)
    plt.xlabel('时间/h')
    plt.ylabel('空气质量/AQI')
    plt.show()


def main():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    data = pd.read_csv('西安未来十五天天气.csv', encoding='gb2312')
    data_2 = pd.read_csv('西安当天天气.csv', encoding='gb2312')
    tem_chart_of_the_fifteenth(data)  # 绘制未来十五天天气温度
    weayher_chart_of_the_day(data_2)  # 绘制当天天气温度变化
    daily_relative_humidity(data_2)  # 绘制当天相对湿度变化
    air_quality_chart_of_the_day(data_2)  # 绘制当天空气质量变化
    fifteenday_weather_map(data)


if __name__ == '__main__':
    main()
