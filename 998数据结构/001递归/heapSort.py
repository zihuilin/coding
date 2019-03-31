import math

def parent(child_index):
    return (child_index - 1)//2


def left_child(parent_index):
    return parent_index * 2 + 1


def right_child(parent_index):
    return parent_index * 2 + 2


heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_size = len(heap)


def print_heap(heap, heap_size):
    print("=======================HEAP PRINT======================")
    height = math.ceil(math.sqrt(heap_size))
    h = 1
    for i in range(heap_size):
        if i == math.pow(2, h-1) - 1:
            for b in range(int(math.pow(2, height - h)) - 1):
                print("  ", end='')
        print("%2d" % heap[i], end='')
        for b in range(int(math.pow(2, height-h+1)) - 1):
            print("  ", end='')
        if i==math.pow(2, h) - 2:
            print()
            h = h + 1
    print()
    print("=======================================================")


print_heap(heap, heap_size)

def max_heapify(heap, heap_size, i):
    lc = left_child(i)
    rc = right_child(i)
    max_index = i
    if lc < heap_size and heap[lc] > heap[max_index]:
        max_index = lc
    if rc < heap_size and heap[rc] > heap[max_index]:
        max_index = rc
    if max_index != i:
        heap[i], heap[max_index] = heap[max_index], heap[i]
        max_heapify(heap, heap_size, max_index)

heap[0] = 5

max_heapify(heap, heap_size, 0)
print_heap(heap, heap_size)

def build_heap(heap,heap_size):
    for i in range(int(heap_size/2 - 1), -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(a):
    size = len(a)
    build_heap(a, size)
    for i in range(size-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        size = size - 1 
        max_heapify(a, size, 0)

a = [2, 3, 8, 9, 4, 1, 7]

heap_sort(a)
print(a)
print_heap(a, len(a))
