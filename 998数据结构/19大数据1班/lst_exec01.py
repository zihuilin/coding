lst = []

for i in range(1,100):
    lst.append(i)

sum = 0
for i in range(len(lst)):
    sum += lst[i]

print(sum)   #sum is 4950

i = int(input())  # 输入一个下标
print(lst[i]) 

print(len(lst)-1) # 得到最后一个元素的下标为98
print(lst[-1])  # 得到最后一个元素
