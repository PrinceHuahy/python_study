from itertools import combinations

Data_1 = {
    ('moneyline_home', 0, 200, 'event', 'dealer_a', '2.29'): [
        11, 21, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63,
        64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98, 99
    ]
}
Data_2 = {
    ('handicap_away', 0.5, 200, 'event', 'dealer_b', '1.99'): [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23,
        24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48,
        49, 50, 56, 57, 58, 59, 60, 67, 68, 69, 70, 78, 79, 80, 89, 90, 100
    ]
}
Data_3 = {
    ('moneyline_draw', 0, 200, 'event', 'dealer_a', '3.45'):
        [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
}
Data_4 = {
    ('moneyline_away', 0, 200, 'event', 'dealer_a', '3.20'): [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26,
        27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 57, 58, 59,
        60, 68, 69, 70, 79, 80, 90
    ]
}
Data_5 = {
    ('handicap_away', 0.25, 150, 'event', 'dealer_b', '1.93'):
        [1, 12, 23, 34, 45, 56, 67, 78, 89, 100],
    ('handicap_away', 0.25, 200, 'event', 'dealer_b', '1.93'): [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26,
        27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 57, 58, 59,
        60, 68, 69, 70, 79, 80, 90
    ]  # 需要注意的是有的数据里有两个dealer,但是肯定一样.
}
Data_6 = {
    ('handicap_home', 0, 100, 'event', 'dealer_b', '1.67'):
        [1, 12, 23, 34, 45, 56, 67, 78, 89, 100],
    ('handicap_home', 0, 200, 'event', 'dealer_b', '1.67'): [
        11, 21, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63,
        64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98, 99
    ]
}
Data_7 = {
    ('handicap_away', 0.75, 50, 'event', 'dealer_b', '4.08'):
        [11, 22, 33, 44, 55, 66, 77, 88, 99],
    ('handicap_away', 0.75, 200, 'event', 'dealer_b', '4.08'): [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23,
        24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48,
        49, 50, 56, 57, 58, 59, 60, 67, 68, 69, 70, 78, 79, 80, 89, 90, 100
    ]
}
Data_8 = {
    ('handicap_home', 0.5, 200, 'event', 'dealer_a', '2.01'): [
        1, 11, 12, 21, 22, 23, 31, 32, 33, 34, 41, 42, 43, 44, 45, 51, 52, 53,
        54, 55, 56, 61, 62, 63, 64, 65, 66, 67, 71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        100
    ]
}

Target_map = [i for i in range(1, 101)]
L = [Data_1, Data_2, Data_3, Data_4, Data_5, Data_6, Data_7, Data_8]


def translate_dict(x):
    # if input data's keys == 2,let (key1,key2) match set(value1 + value2)
    if len(list(x.keys())) == 2:
        l1 = []
        for i in x:
            l1.append(i)
        t = tuple(l1)
        # t = (key1,key2)
        l2 = []
        for i in x.values():
            l2.extend(i)
            # combine value1 and value2
        l2 = list(set(l2))
        # remove the duplicate values
        x = dict()
        x[t] = l2
        return x
    else:
        return x


def div_keys_values(L):
    for i in range(len(L)):  # let double key data like data567 combine keys and values.
        L[i] = translate_dict(L[i])

    L_keys = []
    L_values = []
    for i in L:
        for j in i:
            L_keys.append(j)
            L_values.append(i[j])
    return L_keys, L_values


def combine(temp_list, n):
    '''根据n获得列表中的所有可能组合（n个元素为一组）'''
    temp_list2 = []
    for c in combinations(temp_list, n):
        temp_list2.append(c)
    return temp_list2


def show_dic(input_tuple):
    # get the dict.keys and return {key:value}
    for i in L:
        for k, v in i.items():
            if input_tuple == k:
                return i


def main(L):
    L_keys, L_values = div_keys_values(L)  # separate all keys and values
    end_list1 = []  # create new list
    for i in range(len(L_keys)):  # for loop
        end_list1.extend(combine(L_keys, i))  # add each element in list not the list-self
        # first time return zero elements list
        # then return 1 elements list,2 ele, 3 ele, ...

    end_list2 = []
    for i in range(len(L_values)):
        # same as before.
        end_list2.extend(combine(L_values, i))
    result = []
    for i in range(len(end_list2)):
        l0 = []
        for j in end_list2[i]:
            l0.extend(j)
        if sorted(set(l0)) == Target_map:
            result.append(end_list1[i])

    # show_dic(('moneyline_home', 0, 200, 'event', 'dealer_a', '2.29'))
    list_2 = []
    for i in result:
        list_1 = []
        for j in i:
            list_1.append(show_dic(j))
        list_2.append(list_1)
    return list_2


if __name__ == '__main__':
    jieguo = main(L)
    print(jieguo)

'''
('moneyline_home', 0, 200, 'event', 'dealer_a', '2.29')
('handicap_away', 0.5, 200, 'event', 'dealer_b', '1.99')
'''

# 最终结果jieguo = L_new.要求格式一样,结果中的每一条组合数据中key[4]的值不能一样

# L_new = [[{
#     ('moneyline_home', 0, 200, 'event', 'dealer_a', '2.29'): [
#         2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26,
#         27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 57, 58, 59,
#         60, 68, 69, 70, 79, 80, 90
#     ]
# }, {
#     ('handicap_away', 0.75, 50, 'event', 'dealer_b', '4.08'):
#         [2, 13, 24, 35, 46, 57, 68, 79, 90],
#     ('handicap_away', 0.75, 200, 'event', 'dealer_b', '4.08'): [
#         1, 11, 12, 21, 22, 23, 31, 32, 33, 34, 41, 42, 43, 44, 45, 51, 52, 53,
#         54, 55, 56, 61, 62, 63, 64, 65, 66, 67, 71, 72, 73, 74, 75, 76, 77, 78,
#         81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99,
#         100
#     ]
# }],
#     [{
#         ('handicap_home', 0.5, 200, 'event', 'dealer_a', '2.01'): [
#             1, 11, 12, 21, 22, 23, 31, 32, 33, 34, 41, 42, 43, 44, 45, 51,
#             52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 67, 71, 72, 73,
#             74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91,
#             92, 93, 94, 95, 96, 97, 98, 99, 100
#         ]
#     }, {
#         ('handicap_away', 0.5, 200, 'event', 'dealer_b', '1.99'): [
#             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19,
#             20, 23, 24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39,
#             40, 45, 46, 47, 48, 49, 50, 56, 57, 58, 59, 60, 67, 68, 69,
#             70, 78, 79, 80, 89, 90, 100
#         ]
#     }]]
''''''
# each data have key and values. some data have two keys and values,
# make sure those data that have two keys will not combine each others.
