a = [3,5,9,20,1,7,67,6,8,4,2]

def _merge(array, start, middle, end):
    len1 = middle - start + 2
    len2 = end - middle + 1
    array1 = [0] * len1
    array2 = [0] * len2

    for i in range(len1-1):
        array1[i] = array[start + i]

    for j in range(len2-1):
        array2[j] = array[middle + j + 1]
    
    if array[middle] > array[end]:
        max = array[middle] + 1
    else:
        max = array[end] + 1

    array1[len1-1] = max;
    array2[len2-1] = max;

    i = 0
    j = 0
    for k in range(start, end+1):
       if array2[j] < array1[i]:
            array[k] = array2[j]
            j = j + 1
       else:
            array[k] = array1[i]
            i = i + 1


def _merge_sort(array, start, end):
    if start >= end:
       return
    else :
        middle = int((start + end)/2)
        _merge_sort(array, start, middle) # middle as the end
        _merge_sort(array, middle+1, end)
        _merge(array, start, middle, end)


def merge_sort(array):
	_merge_sort(array, 0, len(array)-1)


merge_sort(a)
print(a)
    

