
def merge(lst, start, middle, end):
    len1 = middle - start + 1
    len2 = end - middle
    array1 = [0] * len1  #长度为len1
    array2 = [0] * len2  #长度为len2
    for i in range(0, len1): # 0->len1-1
        array1[i] = lst[start + i]
    for j in range(0, len2): # 0->len2-1
        array2[j] = lst[middle + j + 1]

    i = 0
    j = 0
    for k in range(start, end+1):
        if i==len1 or (j!=len2 and array1[i]>array2[j]) :
            lst[k] = array2[j]
            j = j + 1
        else:
            lst[k] = array1[i]
            i = i + 1
lst = [1,3,2,4]

merge(lst, 0, 1, 3)
print(lst)
