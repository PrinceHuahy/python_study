# -*- coding = utf-8 -*-
# @Time : 2022/6/17 10:32
# @Author : 最帅杰尼龟(zsjng)
# @File : read_txt.py.py
# @Software : PyCharm
import xlwt
def show_ori():
    with open('last.txt', 'r', encoding='utf-8') as f:
        list_1 = list(f)
    a = ''
    # print(list_1)
    for i in list_1:
        i = i.replace('!!!!!', ',')
        i = i.replace('positive mean ', 'positive')
        i = i.replace('number positives ', 'np')
        i = i.replace('negative mean ', 'negetive')
        i = i.replace('SHAP values for ll: mean-', 'll')
        a = i.replace('].', '],')

    b = a.split(',')
    # print(b,type(b))
    j = 0
    datalist = []
    while j < len(b) - 6:
        data = []
        for i in range(j, j + 6):
            b[i] = b[i].strip()
            print(b[i], end=',')
            data.append(b[i].strip())
            # print(data)
        j += 6
        print('\n')



def change():
    test = []
    result = []
    test_new = []
    with open('test.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():  # readlines以列表输出文件内容
            line = line.replace("\n", "").replace("\n", "")  # 改变元素，去掉，和换行符\n,tab键则把逗号换成"/t",空格换成" "
            result.append(line)
    for i in result:
        # print(i)
        test.append(i.split(','))
    # print(conbine_data.py)
    for i in test:
        i_new = []
        for j in i:
            j = j.replace('SHAP values for ll: mean-[', '')
            j = j.replace('positive[', '')
            j = j.replace('np[', '')
            j = j.replace('negetive[', '')
            j = j.replace('number negatives [', '')
            j = j.replace('ll[', '')
            j = j.replace(", ''", '')
            j = j.replace(']', '')
            i_new.append(j)
            test_new.append(i_new)
        print(test_new[0])
    return test_new


def save_data(datalist, savepath):
    print('save...')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建workbook对象
    sheet = book.add_sheet('file', cell_overwrite_ok=True)
    col = ('file_name', 'SHAP values', 'positive', 'number positives', 'negative', 'number negative')
    for i in range(0, 6):
        sheet.write(0, i, col[i])
    # 写入第一行
    for i in range(2, 2001, 2):
        print(f'第{i + 1}条')
        data = datalist[i]
        for j in range(0, 6):
            if i % 2 == 0:
                sheet.write(int(i / 2), j, data[j])
            else:
                continue
    book.save(savepath)

show_ori()
# save_data(change(), './conbine_data.py.xls')
