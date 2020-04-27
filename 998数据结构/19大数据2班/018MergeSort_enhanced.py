import random
import time

n = 230000
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
def merge(lst, start, middle, end):
    len1 = middle - start + 2 #多一个位置给哨兵
    len2 = end - middle + 1   #多一个位置给哨兵
    array1 = [0] * len1  #长度为len1
    array2 = [0] * len2  #长度为len2
    for i in range(0, len1-1): # 0->len1-2
        array1[i] = lst[start + i]
    for j in range(0, len2-1): # 0->len2-2
        array2[j] = lst[middle + j + 1]
    if lst[middle] > lst[end]:
        max = lst[middle] + 1
    else:
        max = lst[end] + 1

    array1[len1-1] = max
    array2[len2-1] = max

    i = 0
    j = 0
    for k in range(start, end+1):
        if array1[i]>array2[j]:
            lst[k] = array2[j]
            j = j + 1
        else:
            lst[k] = array1[i]
            i = i + 1

# 作用：将start到end之间的所有元素排序
def merge_sort(lst, start, end):
    if end - start < 5:  #出口：只有三个元素
        #插入排序这3个元素
        for i in range(start+1, end+1):
            temp = lst[i]
            j = i-1
            while j>=start:
                if temp < lst[j]:
                    lst[j+1] = lst[j]
                else:
                    break
                j = j - 1
            lst[j+1] = temp; # 插入
        return
    else:
        middle = (end + start)//2
        merge_sort(lst, start, middle) #排好第1部分
        merge_sort(lst, middle+1, end) #排好第2部分
        merge(lst, start, middle, end)


merge_sort(lst,0,len(lst)-1)
time = time.time() - start_time   #选择排序执行的时长（秒）

#print(lst)  #排序好之后的list
print("%.8f" % time)
