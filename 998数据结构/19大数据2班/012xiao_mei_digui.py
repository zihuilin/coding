
def xm(n):
    #先判断递归出口
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        #递归表达式
        return xm(n-2) + xm(n-1)

print(xm(40))
