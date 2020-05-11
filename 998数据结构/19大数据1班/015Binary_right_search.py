lst = [-1,0,0,0,0,0,0,1]

def binary_left_serach(lst, target):
    left = 0
    right = len(lst) - 1 

    while left < right:  #当搜索区域只有1个时
        #mid是第2部分的第1个元素的下标
        mid = (left + right + 1) // 2
        if lst[mid] == target : 
            left = mid
        elif lst[mid] > target:
            # 把问题规模缩小为左半边
            right = mid - 1
        elif lst[mid] < target:
            # 把问题规模缩小为右半边
            left = mid + 1

    if lst[right] == target:
        return right 
    else:
        return -1

i = binary_left_serach(lst, 0) #在lst里搜索元素为0的下标
print(i)
print(len(lst))

