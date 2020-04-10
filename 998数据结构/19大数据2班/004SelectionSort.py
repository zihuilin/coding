import time

lst = [3,7,2,9,8,1,2]

print(lst)
start_time = time.time()

for k in range(0, len(lst)-1): # k从0 到len-2做循环
    #求0到len-1的最小值
    minIndex = k    # 假设第k个元素为最小值(k为最前面的元素)
    for i in range(k+1, len(lst)):  # 让i从下标k循环到len-1
        # 判断i所在的元素是否比maxIndex所在元素小
        if (lst[i] < lst[minIndex]) :
            minIndex = i  # 如果是，就变量最值所在的位置为i
    t = lst[minIndex]       #对调第1步： 将最大值放在t里
    lst[minIndex] = lst[k]  #对调第2步： 将原来最后位置上的值放到maxIndex上
    lst[k] = t              #对调第3步： 将t里的最大值放到最后的位置上

time = time.time() - start_time

print(lst)
print("%.8f" % time)
