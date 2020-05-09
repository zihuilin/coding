
lst = [1,3,2,4,5,7,6,8]

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

merge(lst,0,1,3)
print(lst) # 1,2,3,4,5,7,6,8
merge(lst,4,5,7)
print(lst) # 1,2,3,4,5,6,7,8
