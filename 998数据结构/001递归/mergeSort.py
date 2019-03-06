a = [3,5,9,1,7,6,8,4,2]

def _merge(array, start, middle, end):
    len1 = middle - start + 1
    len2 = end - middle
    array1 = [0] * len1
    array2 = [0] * len2

    for i in range(len1):
        array1[i] = array[start + i]

    for j in range(len2):
        array2[j] = array[middle + j + 1]

    i = 0
    j = 0
    for k in range(start, end+1):
       if i == len1 and j == len2:
            break
       if i==len1 or (j!=len2 and array2[j] < array1[i]):
            array[k] = array2[j]
            j = j + 1
       else:
            array[k] = array1[i]
            i = i + 1
       k = k + 1


def _merge_sort(array, start, end):
	if start != end:
		length = end - start + 1
		middle = int(start + length/2)
		if length%2 == 0:
			middle = middle - 1
		_merge_sort(array, start, middle)
		_merge_sort(array, middle+1, end)
		_merge(array, start, middle, end)


def merge_sort(array):
	_merge_sort(array, 0, len(array)-1)


merge_sort(a)
print(a)
    

