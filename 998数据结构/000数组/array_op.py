# -*- coding: utf-8

'''
数组的初始化和元素访问
'''
# 直接给各个出元素的初始化方式
A = [[1,3,5],[2,7,11],[13,15,17]]
B = [[9,8,7],[6,5,4],[3,2,1]]
N = 3

print(A) #打印整个2维数组
print(A[0]) #打印第1行
# 打印A的第1列？
for row in A:
    print(row[0])

print()

print(A[0][1]) #第1行，第2个元素

# 用某个值填充整个2维数组 
r = 3 # 3行
c = 4 # 4列
AA = [[0]*c for i in range(r)] # 不能使用a= [ [0] *m ] * n

AA[2][3] = 4

print("AA[2][3]: %d" % AA[2][3])
print("AA[1][3]: %d" % AA[1][3])

# 从程序外输入2维数组
'''
r = int(input('要输入的2维数组的行数：'))
AAA = []
print('请输入2维数组的各行，行内的元素用空格分开：')
for i in range(r):
    AAA.append([int(j) for j in input().split()])

print("AAA[1][1]: %d" % AAA[1][1])
'''

# 遍历数组
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end=' ')
    print()

