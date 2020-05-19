lst = [0,1]

def binary_right_serach(lst, target):
    left = 0
    right = len(lst) - 1 

    while left + 1 < right:  #当搜索区域只有2个时
        mid = (left + right) // 2
        if lst[mid] == target : 
            left = mid
        elif lst[mid] > target:
            # 把问题规模缩小为左半边
            right = mid
        elif lst[mid] < target:
            # 把问题规模缩小为右半边
            left = mid
    if lst[right] == target:
        return right
    elif lst[left] == target:
        return left
    else:
        return -1

i = binary_right_serach(lst, 0) #在lst里搜索元素为0的下标
print(i)
print(len(lst))

