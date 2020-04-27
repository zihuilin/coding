lst = [6,4,9,1,11,18,12]

for i in range(1, len(lst)): #i: 1->len-1
    #i是当前要插入的位置
    temp = lst[i] # temp里存放的是要插入的元素
    j = i - 1
    while j >= 0 :
        if lst[j] > temp :
            lst[j+1] = lst[j] #把j位置上的元素后移
        else: #找到了要插入的位置
            break
        j = j - 1
    lst[j+1] = temp #把要插入的元素放在j位置后面

print(lst)
