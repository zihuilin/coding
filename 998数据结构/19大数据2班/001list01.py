# 声明一个空的数组
lst = []  
#print(len(lst))

#声明一个10个元素的数组
lst2 = [0] * 10 
#print(len(lst2))

#将下标为1的元素赋值为2
lst2[1] = 2
#print(lst2[1])

#将第1个元素赋值为1
lst2[0] = 1

#将前两个元素的值的和，赋值给第3个元素
lst2[2] = lst2[0] + lst2[1]

# 遍历数组lst2，每次遍历时将元素放到i里
'''
for i in lst2:
    print(i)
'''

# 将1到10放到lst里
'''
for i in range(1,11):
    lst.append(i)
'''


lst = [i in range(1,11)]

for i in lst:
    print(i)
