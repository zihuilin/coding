lst = [3,7,2,9,8,1,2]

for k in range(0, len(lst)-1):
    for i in range(len(lst)-2,k-1, -1):
        if lst[i] > lst[i+1]: #如果i下标的元素比较大
            # 对调下标i的元素和下标i+1的元素
            lst[i],lst[i+1] = lst[i+1],lst[i] 

print(lst)  #排序好之后的list

