import random

n = int(input('n='))
a = [0] * n

for i in range(n):
    a[i] = random.randrange(0,10000000)

for i in range(n):
    temp = a[i]
    j = i - 1
    while j >= 0 :
        if temp > a[j] :
            a[j+1] = a[j]
        else :
            break;
        j = j - 1
    a[j+1] = temp

for e in a :
    print(e, end=' ')
print()
