import random
import time

n = 2300
lst =[]
for i in range(n): #填充0到9至lst
    lst.append(i)
#print(random.randint(0,9))
#print(lst)  #打散之前
for i in range(n): #对于遍历到的每个位置
    r = random.randint(0, len(lst)-1) # 随机的位置
    # 对调i位置和r位置的元素
    t = lst[i]
    lst[i] = lst[r]
    lst[r] = t
#print(lst)  #打散之后
#执行选择排序
start_time = time.time()

for k in range(len(lst)-1, 0, -1): # k从len-1 到 1做循环
    #求0到len-1的最大值
    maxIndex = 0    # 假设第1个元素为最大值
    for i in range(1, k+1):  # 让i从下标2循环到k
        # 判断i所在的元素是否比maxIndex所在元素大
        if (lst[i] > lst[maxIndex]) :
            maxIndex = i  # 如果是，就变量最大值所在的位置为i
    t = lst[maxIndex]       #对调第1步： 将最大值放在t里
    lst[maxIndex] = lst[k]  #对调第2步： 将原来最后位置上的值放到maxIndex上
    lst[k] = t              #对调第3步： 将t里的最大值放到最后的位置上

time = time.time() - start_time   #选择排序执行的时长（秒）

#print(lst)  #排序好之后的list
print("%.8f" % time)
