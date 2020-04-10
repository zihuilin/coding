# lst里放入1到99这些元素
lst = [ i for i in range(1, 100)]

sum = 0
for i in lst:
  sum = sum + i
print(sum)

# 用户输入下标放到i里
i = int(input())
# 输出下标i对应的元素
print(lst[i])
