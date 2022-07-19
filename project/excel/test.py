# coding=utf-8
# @Time : 2022/7/19 15:52
# @Author : zsjng
# @File : test.py
# @Software : PyCharm

input = [904, 907, 908, 909, 910, 912, 918, 919, 920, 920]


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


print(find_t1(input))


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


print(find_tn(input))
