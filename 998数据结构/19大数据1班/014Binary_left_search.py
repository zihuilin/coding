lst = [-21,0,0,0,0,0,3,6,9,10,100]

def binary_left_serach(lst, target):
    left = 0
    right = len(lst) - 1 

    while left < right:  #当搜索区域只有1个时
        mid = (left + right) // 2
        if lst[mid] == target : 
            right = mid
        elif lst[mid] > target:
            # 把问题规模缩小为左半边
            right = mid - 1
        elif lst[mid] < target:
            # 把问题规模缩小为右半边
            left = mid + 1
    #走到这里，搜索失败
    if lst[left] == target:
        return left
    else:
        return -1

i = binary_left_serach(lst, 0) #在lst里搜索元素为0的下标
print(i)

