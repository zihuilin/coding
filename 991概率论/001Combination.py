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

#print(cb(8,5))

print(cb(8,3) * (cb(4,3) + cb(2,1)*cb(4,2)))
print((cb(6,3) + cb(2,1)*cb(6,2))*cb(6,3))
print(cb(7,3)*cb(5,3) + cb(7,3)*cb(5,2) + cb(7,2)*cb(5,3))

print(cb(6,3))
