import random

n = int(input('n='))
a = [0] * n

for i in range(n):
    a[i] = random.randrange(0,1000000)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index = j;
    temp = a[i]
    a[i] = a[min_index]
    a[min_index] = temp

for e in a:
    print(e, end=' ')
print()
