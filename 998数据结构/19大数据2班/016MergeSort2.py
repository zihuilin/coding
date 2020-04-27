
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
    if start == end:  #出口：只有一个元素
        return
    else:
        middle = (end + start)//2
        merge_sort(lst, start, middle) #排好第1部分
        merge_sort(lst, middle+1, end) #排好第2部分
        merge(lst, start, middle, end)

#lst = [1,3,2,4]
lst = [3,7,2,0,-2,9,8,1,2]

#merge(lst, 0, 1, 3)
merge_sort(lst,0,len(lst)-1)
print(lst)
