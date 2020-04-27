import random
import time

n = 1000
lst = [0] * n
for i in range(0, len(lst)): #循环n次：0->len-1
    lst[i] = i #元素和下标一样

random.seed(time.time()) #用当前时间作为seed
for i in range(0, len(lst)):
    r = random.randint(0, len(lst)-1); #随机的位置r
    lst[i],lst[r] = lst[r],lst[i]; #对调下标i和r对应的元素

start_time = time.time()
# k: len-1 -> 1
for k in range(len(lst)-1, 0, -1):
    # i: 0 -> k-1
    for i in range(0, k):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]

end_time = time.time()
print(end_time-start_time)
#print(lst)
