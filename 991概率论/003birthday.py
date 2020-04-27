n = 1
p = 1
day = 365
while p >= 0.05 :
    day = 365 - n
    n = n + 1
    p = p * day / 365
    print(str(n) + " : " + str(p))


