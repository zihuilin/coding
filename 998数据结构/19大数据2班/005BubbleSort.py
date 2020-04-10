import random
import time

n = 5000
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

for k in range(len(lst)-1, -1, -1):
    for i in range(0, k):
        if lst[i] > lst[i+1]: #如果i下标的元素比较大
            # 对调下标i的元素和下标i+1的元素
            lst[i],lst[i+1] = lst[i+1],lst[i] 

time = time.time() - start_time   #选择排序执行的时长（秒）

#print(lst)  #排序好之后的list
print("%.8f" % time)

