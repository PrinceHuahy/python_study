# coding=utf-8
# @Time : 2022/7/14 16:02
# @Author : zsjng
# @File : read_map.py
# @Software : PyCharm

def read_map(filename):
    #     sx, sy = 0, 0 #start location
    #     gx, gy = 0, 0 #target location
    ox, oy = [], []  # obstacle location
    with open(filename) as file:
        i = 0
        while line := file.readline():
            for j, char in enumerate(line):
                if char == 'W':
                    ox.append(j)
                    oy.append(i)
                else:
                    if char == 'S':
                        sx = j
                        sy = i
                    elif char == 'T':
                        gx = j
                        gy = i
                    else:
                        continue
            i += 1
    for i in range(0,max(oy)):
        ox.append(i)
        oy.append(0)
        ox.append(i)
        oy.append(361)
    for i in range(0,max(ox)):
        ox.append(0)
        oy.append(i)
        ox.append(max(ox))
        oy.append(i)
    return sx, sy, ox, oy, gx, gy


# 将txt文本的内容转化为坐标。

# if __name__ == '__main__':
#     # sx,sy,ox,oy,gx,gy = read_map('data_1.txt')
#
#     sx = -5.0
#     sy = -5.0
#     gx = 50
#     gy = 50
#     ox = []
#     oy = []
#     for i in range(-10, 60):
#         ox.append(i)
#         oy.append(-10)  # y坐标-10的一行-10~60的坐标添加到列表并显示为黑色障碍物
#     for i in range(-10, 60):
#         ox.append(i)
#         oy.append(60)  # y坐标60的一行-10~60的坐标添加到列表并显示为黑色障碍物
#     for i in range(-10, 61):
#         ox.append(-10)
#         oy.append(i)  # x坐标-10的一列-10~61的坐标添加到列表并显示为黑色障碍物
#     for i in range(-10, 61):
#         ox.append(60)
#         oy.append(i)  # x坐标60的一列-10~61的坐标添加到列表并显示为黑色障碍物
#     for i in range(-10, 40):
#         ox.append(20)
#         oy.append(i)  # x坐标20的一列-10~40的坐标添加到列表并显示为黑色障碍物
#     for i in range(0, 40):
#         ox.append(40)
#         oy.append(60 - i)  # x坐标40的一列20~60的坐标添加到列表并显示为黑色障碍物
#
#     print('sx = ', sx)
#     print('sy = ', sy)
#     print('ox = ', ox)
#     print('oy = ', oy)
#     print('gx = ', gx)
#     print('gx = ', gy)

# point = 29
# step = (29 // 5)
# point1 = range(0,step)
# point2 = range(step,step*2)
# point3 = range(step*2,step*3)
# point4 = range(step*3,step*4)
# point5 = range(step*4,step*5)
# point6 = range(step*5,point)
#
# print(point1,point6)