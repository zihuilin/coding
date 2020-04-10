lst = []

lst.append(1) #第1级台阶1种走法，不用算
lst.append(2) #第2级台阶2种走法，不用算

n = int(input())

for i in range(2, n):   #从下标2，算到n-1
    lst.append(lst[i-1] + lst[i-2])

print(lst[n-1])
