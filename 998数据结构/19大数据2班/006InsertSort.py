
lst=[1,3,7,8,10,4,9,5,6];
# 当前要插入“4”这个元素
# i是要插入元素的位置
i = 5;
#1. 空出i这个位置
temp = lst[i]  #把"4"把到temp里
#2 遍历i前面的元素，完成插入操作
for j in range(i-1, -1, -1):
    if temp < lst[j]:
        lst[j+1] = lst[j]
    else:
        break;
lst[j+1] = temp; # 插入

print(lst)
#完成上面的1和2操作，就可以把4插入到前面了。
