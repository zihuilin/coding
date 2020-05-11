lst = [-21,-3,0,3,6,9,10,100]

def binary_serach(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:  #当搜索区域没有小到0
        mid = (left + right) // 2
        if lst[mid] == target : 
            return mid;
            break;
        elif lst[mid] > target:
            # 把问题规模缩小为左半边
            right = mid - 1
        elif lst[mid] < target:
            # 把问题规模缩小为右半边
            left = mid + 1
    #走到这里，搜索失败
    return -1

i = binary_serach(lst, 100) #在lst里搜索元素为0的下标
print(i)

