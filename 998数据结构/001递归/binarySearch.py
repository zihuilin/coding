
a = [1,3,5,7,8,12,45,55,57,78]

def binary_search(array, start, end, value):
    NOT_FOUND = -1
    if start == end:
        if array[start] == value:
            return start
        else:
            return NOT_FOUND;
    else:
        length = end - start + 1
        middle = int(start + length/2)
        if length%2 != 0:
            middle = middle + 1
        if value > array[middle]:
            return binary_search(array, middle+1, end, value)
        else:
            return binary_search(array, start, middle-1, value)


print(binary_search(a,0,len(a)-1,8))


