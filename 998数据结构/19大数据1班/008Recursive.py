
def m(a,b): #计算a*b的结果
    #1. 判断递归出口到了没？
    if b == 1:
        #如果到了，直接返回结果
        return a
    else:
        #2. 如果没到递归出口
        #使用递推式子解决问题
        return m(a,b-1) + a

print(m(2,3))  #打印：6
