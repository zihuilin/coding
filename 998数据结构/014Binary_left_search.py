lst = [-21,0,0,0,0,0,3,6,9,10,100]
lst = [0,0,0,0,0,3,6,9,10,100]
lst = [0,0,0,0,0,3]

def binary_left_serach(lst, target):
    left = 0
    right = len(lst) - 1 

    while left + 1 < right:  #当搜索区域只有2个时
        mid = (left + right) // 2
        if lst[mid] == target : 
            right = mid
        elif lst[mid] > target:
            # 把问题规模缩小为左半边
            right = mid
        elif lst[mid] < target:
            # 把问题规模缩小为右半边
            left = mid
    if lst[left] == target:
        return left
    elif lst[right] == target:
        return right
    else:
        return -1

i = binary_left_serach(lst, 0) #在lst里搜索元素为0的下标
print(i)

