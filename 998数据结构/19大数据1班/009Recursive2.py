
lst = [0]*100

#求n级台阶的上法总数
def taijie(n):
    #出口
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if lst[n] == 0:
            lst[n] = taijie(n-1) + taijie(n-2)
        return lst[n]

print(taijie(40))
