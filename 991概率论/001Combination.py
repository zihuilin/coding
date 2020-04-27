cb_dict = {}

def cb (n, r):
    if r==0:
        return 1  #n个里取0个，只有1种取法
    elif n==0:
        return 0  #0个里取r个，只有0种取法
    #n为8,r为5组织一个字符串："8,5"
    key = str(n) + "," + str(r)
    if key not in cb_dict:
        cb_dict[key] = cb(n-1, r-1) + cb(n-1, r) 
    return  cb_dict[key]

def pm(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

sp = 6 * 6 * 6 * 6 * 6
a = pm(6)/sp
b = (6*cb(5,2)*5*4*3)/sp
c = (cb(6,2)*4*cb(5,2)*cb(3,2))/sp
d = (6*cb(5,3)*5*4)/sp
e = (6*cb(5,3)*5)/sp
f = (6*cb(5,4)*5)/sp
g = 6/sp
print("%.5f" % a)
print("%.5f" % b)
print("%.5f" % c)
print("%.5f" % d)
print("%.5f" % e)
print("%.5f" % f)
print("%.5f" % g)

#print(cb(8,5))
'''
print(cb(8,3) * (cb(4,3) + cb(2,1)*cb(4,2)))
print((cb(6,3) + cb(2,1)*cb(6,2))*cb(6,3))
print(cb(7,3)*cb(5,3) + cb(7,3)*cb(5,2) + cb(7,2)*cb(5,3))

print(cb(6,3))
'''
