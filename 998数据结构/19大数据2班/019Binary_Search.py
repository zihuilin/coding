lst = [1,2,3,4,5,6,7,8,9,10]
t = 2 

def binary_search(lst, t) :
    start = 0
    end = len(lst)-1
    while start <= end : #搜索还没有失败的时候
        middle = (end + start)//2
        if lst[middle] == t :
            return middle
        elif lst[middle] > t :
            end = middle - 1  #更新上界
        elif lst[middle] < t :
            start = middle + 1 #更新下界
    return -1 #while循环结束，说明没有找到t

print(binary_search(lst,t))
