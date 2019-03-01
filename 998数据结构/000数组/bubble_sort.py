import time
import random

n = int(input('n='))
a = [0] * n

for i in range(n):
    a[i] = random.randrange(0,1000000)

start_time = time.time()

for i in range(n):
    for j in range(i+1,n):
        if a[j] < a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

end_time = time.time()

for e in a:
    print(e, end=' ')
print ('\ntime: %f\n' % (end_time - start_time))

