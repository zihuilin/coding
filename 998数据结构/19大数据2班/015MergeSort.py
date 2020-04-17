
def merge(lst, start, middle, end):
    #1 将第1部分和第2部分分别拷贝到两个lst里
    #1.1 计算第1部分的长度和第2部分的长度
    len1 = middle - start + 1
    len2 = end - middle
    #1.2 声明两个长度合适的lst
    array1 = [0] * len1  #长度为len1
    array2 = [0] * len2  #长度为len2
    #1.3 用两个循环，把第1部分的元素和第2部分的元素拷贝到两个lst里
    for i in range(0, len1): # 0->len1-1
        array1[i] = lst[start + i]
    for j in range(0, len2): # 0->len2-1
        array2[j] = lst[middle + j + 1]
    #print(array1)
    #print(array2)
    #2合并两个lst到原lst里
    #2.1 一个循环，从原lst的start到end
        #2.2 如果array2中的所有元素都放完
        #    或者array1的当前标记元素较小
        #    上面的两个条件只要满足一个
        #    就：放array1中的元素到原list
        #    记得i要自增1
        #2.3 否则就将array2中的元素放到原list
        #    记得j要自增1

lst = [1,3,2,4]

merge(lst, 0, 1, 3)
