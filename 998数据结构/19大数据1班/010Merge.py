
lst [1,3,2,4,5,7,6,8]

def merge(lst,start,mid,end):
    len1 = mid - start + 1  #计算第1部分的长度
    len2 = end - mid        #计算第2部分的长度
    lst1 = [0] * len1
    lst2 = [0] * len2
    #拷贝start到mid里的元素到lst1中
    for i in range(0,len1):
        lst1[i] = lst[start + i]
    #拷贝mid+1到end里的元素到lst2中
    for ....
    i = 1
    j = 1
    for k .... #k: start -> end
    #这部分需要 大家思考怎么做？

print(merge(lst,0,1,3))   # 1,2,3,4,5,7,6,8
print(merge(lst,4,5,7))   # 1,2,3,4,5,6,7,8
