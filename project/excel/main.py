# coding=utf-8
# @Time : 2022/7/19 2:05
# @Author : zsjng
# @File : main.py
# @Software : PyCharm

import pandas as pd

# df1 = pd.read_excel('ori.xlsx')
# df2 = pd.read_excel('sup.xlsx')
# '''
#  0   id         3839 non-null   int64
#  1   read_time  3839 non-null   datetime64[ns]
#  2   epc        3839 non-null   object
#  3   device_id  3839 non-null   object
#  4   ant        3839 non-null   int64
#  '''
# # get support column
# df1['辅助'] = df1['device_id'] + df1['ant'].astype(str)
#
# # combine column choose same column name.
# df_new = pd.merge(df1, df2, on=['辅助'], how='inner')
# print(df_new.head())
# # df_new.to_excel('combine.xlsx')

df = pd.read_excel('combine.xlsx')


# print(df.info())

def change_time_to_sec(time):
    time = str(time)
    # 2022-05-25 16:00:01
    second = int(time[-5:-3]) * 60 + int(time[-2:])
    return second


def find_t1(input):
    while len(input) >= 4:
        time2 = list(range(input[0], input[0] + 4))
        time3 = list(range(input[0] + 4, input[0] + 8))
        time4 = list(range(input[0] + 8, input[0] + 12))
        reta = [i for i in input if i in time2]
        retb = [i for i in input if i in time3]
        retc = [i for i in input if i in time4]
        if len(reta) >= 2 and len(retb) >= 1 and len(retc) >= 1:
            return input[0]
        else:
            input.remove(input[0])
    else:
        return None


def find_tn(input):
    while len(input) >= 4:
        time2 = list(range(input[-1] - 4, input[-1]))
        time3 = list(range(input[-1] - 8, input[-1] - 4))
        time4 = list(range(input[-1] - 12, input[-1] - 8))
        reta = [i for i in input if i in time2]
        retb = [i for i in input if i in time3]
        retc = [i for i in input if i in time4]
        if len(reta) >= 2 and len(retb) >= 1 and len(retc) >= 1:
            return input[-1]
        else:
            input.remove(input[-1])
    else:
        return None


new_list = []
for i in df.loc[:, 'read_time']:
    new_list.append(change_time_to_sec(str(i)))
sec_df = pd.DataFrame(new_list, columns=['read_time'])

df['read_time'] = sec_df['read_time']

# print(df.to_string())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3839 entries, 0 to 3838
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   Unnamed: 0  3839 non-null   int64         
 1   id          3839 non-null   int64         
 2   read_time   3839 non-null   datetime64[ns]
 3   epc         3839 non-null   object        
 4   device_id   3839 non-null   object        
 5   ant         3839 non-null   int64         
 6   辅助          3839 non-null   object        
 7   工位          3839 non-null   int64         
 8   产线          3839 non-null   int64         
dtypes: datetime64[ns](1), int64(5), object(3)
'''
df['工位'] = df['工位'].astype(int).astype(str)
df['epc工位'] = df['epc'] + '-' + df['工位']
# print(df.head(10))

lis = df['epc工位'].unique().tolist()

#
#
# print(lis[0])
epc_list = []
jiepai_list = []
for i in lis:
    key = df.loc[:, 'epc工位'] == i
    epc_list.append(i)
    df3 = df.loc[key].reset_index()
    # print(df3.to_string())
    time_list = df3['read_time'].to_list()
    # print(f'i = {i},len = ', len(time_list))
    if len(time_list) <= 4:
        ans = 0
    else:
        # print(list(time_list))
        count_list = []
        print(time_list)
        tn = find_tn(time_list)
        t1 = find_t1(time_list)
        if t1 is not None and tn is not None:
            ans = tn - t1
        else:
            ans = 0
    jiepai_list.append(ans)
    # print(f'节拍为{ans}')
print('计算完毕')
df_ans = pd.DataFrame(zip(epc_list, jiepai_list), columns=['epc-工位', '节拍'])
df_ans.to_excel('节拍.xlsx')
