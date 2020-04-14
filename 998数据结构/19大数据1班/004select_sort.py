lst = [-2,3,1,6,0,4,2,-1]

#外重循环：解决从0号位置到len-2号位置都是最小值的问题
for k in range(0, len(lst)-1):
    # 1. 选择最小值
    # 1.1 声明一个变量，存放最小值的位置
    min_index = k; # 一开始可以认为k号位置就是最小值的位置
    # 1.2 通过一个遍历，记录最小值的位置
    for i in range(k+1, len(lst)):  #k+1->len-1
        if lst[i] < lst[min_index]:
            min_index = i

    # 2. 把最小值放到它该在的位置上
    # 2.1 通过交换最小值和它该在的位置上的值
    temp = lst[min_index]
    lst[min_index] = lst[k]
    lst[k] = temp

print(lst)
