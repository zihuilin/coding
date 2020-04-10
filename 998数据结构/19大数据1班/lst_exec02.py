lst = []

lst.append(1) # 第一级台阶有1种走法
lst.append(2) # 第二级台阶有2种走法

for n in range(2, 100):
    lst.append(lst[n-1] + lst[n-2])

i = int(input())
print(lst[i-1])
