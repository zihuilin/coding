# 声明一个10个元素的数组
lst = [0] * 10

# 将第1个元素赋值为1
lst[0] = 1

# 输出第0号元素
print(lst[0])

# 得到数组的长度
print(len(lst))

# 遍历所有数组元素,得到的元素放在i里
'''
for i in lst[:]:
    print(i)
'''

#用下标的方式来遍历，下标用i来表示
for i in range(len(lst)):
    print(lst[i])

