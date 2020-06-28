#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

p = 0.05 #单次抓娃娃，抓到的概率
n = 100
plist = []
labels = []

pc = 1.0 #抓不到的概率

for i in range(n-1): #循环n-1次
    labels.append(str(i+1))
    plist.append(p*pc)
    pc = pc * (1 - p)

labels.append(str(n))
plist.append(pc) #pc就是(1-p)^n-1

plt.plot(labels, plist)
plt.show()

