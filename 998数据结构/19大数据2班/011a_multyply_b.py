s = 3
t = 5
sum = 0
'''
for i in range(0, b): #循环b次
    sum = sum + a
'''
def m(a, b): #返回a*b的结构 
    #2. 递归出口
    if b==1:
        return a
    else:
        #1. 给出递归表达式
        return m(a,b-1) + a 

sum = m(s, t)
print(sum)
