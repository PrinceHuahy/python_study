# -*- coding = utf-8 -*-
# @Time : 2022/6/22 19:24
# @Author : 最帅杰尼龟(zsjng)
# @File : 03.for_while_loop.py
# @Software : PyCharm

"""for loop ,while loop"""

'''for loop'''

for i in range(0,5):
    # range(x,y) : x, x+1, x+2, ..., y-2, y-1
    # range(x,y,c): x, x+c, x+2c,...,(x + nc) (x+nc < y)
    print(i, end=' ')
print()
for i in range(2,10,3):
    print(i,end=' ')
print()
'''while loop'''

# for loop works better in limited loop
# while loop works better in unlimited loop

end = 10
while end < 15:
    print(f'end = {end}')
    end += 1

'''continue and break'''

# continue just jump over this loop but still do next loop.
# eg: jump over i == 2 but the for loop will go to i == 3.
# break will end all of loop.

for i in range(20):
    if i % 2 == 0:
        continue
    elif i == 15:
        break
    print(i,end=' ')


