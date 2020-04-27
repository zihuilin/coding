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

sp = cb(52,5)
event = 10 * (4*4*4*4*4 - 4)
p = event / sp
print( "%.5f" % p)
