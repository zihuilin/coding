import random
import time

n = 100000
lst = [0] * n
for i in range(0, len(lst)): #循环n次：0->len-1
    lst[i] = i #元素和下标一样

random.seed(time.time()) #用当前时间作为seed
for i in range(0, len(lst)):
    r = random.randint(0, len(lst)-1); #随机的位置r
    lst[i],lst[r] = lst[r],lst[i]; #对调下标i和r对应的元素
#print(lst)

start_time = time.time()

def merge(lst,start,mid,end):
    len1 = mid - start + 2  #计算第1部分的长度
    len2 = end - mid + 1    #计算第2部分的长度
    lst1 = [0] * len1
    lst2 = [0] * len2
    #拷贝start到mid里的元素到lst1中
    for i in range(0,len1-1):
        lst1[i] = lst[start + i]
    #拷贝mid+1到end里的元素到lst2中
    for j in range(0,len2-1):
        lst2[j] = lst[mid+1+j]

    if lst1[len1-2] > lst2[len2-2]:
        max_value = lst1[len1-2] + 1
    else:
        max_value = lst2[len2-2] + 1
    lst1[len1-1] = max_value
    lst2[len2-1] = max_value

    i = 0
    j = 0
    for k in range(start, end+1): #k: start -> end
        if lst2[j]<lst1[i]:
            lst[k] = lst2[j]
            j = j + 1  #向后移动j
        else:
            lst[k] = lst1[i]
            i = i + 1  #向后移动i

def merge_sort(lst, start, end):
    k = 25
    if end - start <= k:
        for i in range(start+1, end+1):
            temp = lst[i]
            j = i - 1
            while j>=start:
                if lst[j] > temp:
                    lst[j+1] = lst[j]
                else:
                    break
                j = j - 1
            lst[j+1] = temp
        return
    else:
        mid = (start+end)//2
        merge_sort(lst,start,mid)
        merge_sort(lst,mid+1,end)
        merge(lst,start,mid,end)

merge_sort(lst,0, len(lst)-1)
#print(lst)

end_time = time.time()
print(end_time-start_time)
