a = [3,5,9,20,1,7,67,6,8,4,5]

def partition(a, q, r):
    x = a[r]
    i = q - 1
    for j in range(q,r):
        if a[j] < x :
            i = i + 1
            a[i],a[j] = a[j],a[i]
    a[r],a[i+1] = a[i+1],a[r]
    return i+1


def quickSort(a,q,r):
    if q < r:
        p = partition(a, q, r)
        quickSort(a, q, p-1)
        quickSort(a, p+1, r)


def quickSort2(a, q, r):
    x = a[r]
    i = q - 1
    for j in range(q,r):
        if a[j] < x :
            i = i + 1
            a[i],a[j] = a[j],a[i]
    a[r],a[i+1] = a[i+1],a[r]
    p = i+1
    if q < p-1 : quickSort2(a, q, p-1)
    if p+1 < r : quickSort2(a, p+1, r)


quickSort2(a, 0, len(a)-1)
print(a)

