import matplotlib.pyplot as plt

p = 0.1
n = 20
l = []
lables = []
pp = 1.0
for i in range(n):
    lables.append(i+1)
    l.append(p*pp)
    pp = pp * (1 - p)

print(pp)
lables.append(n)
l.append(float(pp))
plt.plot(lables, l)

#plt.xticks(range(n), lables)

plt.show()
