import time

lst = [3,7,2,9,8,1,2]

print(lst)
start_time = time.time()

for k in range(len(lst)-1, 0, -1): # k从len-1 到 1做循环
    #求0到len-1的最大值
    maxIndex = 0    # 假设第1个元素为最大值
    for i in range(1, k+1):  # 让i从下标2循环到k
        # 判断i所在的元素是否比maxIndex所在元素大
        if (lst[i] > lst[maxIndex]) :
            maxIndex = i  # 如果是，就变量最大值所在的位置为i
    t = lst[maxIndex]       #对调第1步： 将最大值放在t里
    lst[maxIndex] = lst[k]  #对调第2步： 将原来最后位置上的值放到maxIndex上
    lst[k] = t              #对调第3步： 将t里的最大值放到最后的位置上

time = time.time() - start_time

print(lst)
print("%.8f" % time)
