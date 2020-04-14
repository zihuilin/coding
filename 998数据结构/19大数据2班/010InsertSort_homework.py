'''
对于while循环，
不管是因为break,
还是因为循环条件不满足,
而结束的循环
要插入的位置都是j+1的位置
'''
lst=[1,3,7,8,10,0,9,5,6];
# 当前要插入“4”这个元素
# i是要插入元素的位置
for i in range(1, len(lst)):
    #1. 空出i这个位置
    temp = lst[i]  #把"4"把到temp里
    #2 遍历i前面的元素，完成插入操作
    j = i-1
    while j>=0:
        if temp > lst[j]:
            lst[j+1] = lst[j]
        else:
            break;
        j = j - 1
    lst[j+1] = temp; # 插入

print(lst)
#完成上面的1和2操作，就可以把4插入到前面了。
