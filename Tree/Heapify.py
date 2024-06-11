def heapsort(alist):
    build_max_heap(alist)       # Вызовем функцию build_max_heap c параметром alist для представления листа в виде пирамиды (heap).
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i) # Вызовем функцию max_heapify, учитывая что новая пирамида имеет размер на единицу меньше. 
                                            #  Установим index=0 для удовлетворения параметрам пирамиды.
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist): # Определим функцию build_max_heap, которая принимает список аргументов и переставляет их в соостветсвии с max heap.
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        # build_max_heap вызывает max_heapify на каждом родительском ноде и проходит до вершины.
        max_heapify(alist, index=start, size=length)
        start = start - 1
# Определим функцию max_heapify, которая принимает индекс и изменяет структуру пирамиды на ноде и снизу от индекса так, 
# чтобы удовлетворять правилам пирамиды.

def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
 
len_arr = int(input())
arr = list(map(int , input().split()))
heapsort(arr)
print(*arr)