# Вариант 1 (с презентации по АЛГОСАМ)
def merge_sort(arr, left, right):
    if left >= right:
        return
    opor_el = (left + right)//2
    merge_sort(arr, left, opor_el)
    merge_sort(arr, opor_el + 1, right)
    merge(arr, left, right, opor_el)
    
def merge(arr, left, right, opor_el):

    left_arr = arr[left : opor_el + 1]
    right_arr = arr[opor_el + 1 : right + 1]


    left_index = 0
    right_index = 0
    sorted_index = left

    while left_index < len(left_arr) and right_index < len(right_arr):

        if left_arr[left_index] <= right_arr[right_index]:
            arr[sorted_index] = left_arr[left_index]
            left_index = left_index + 1
        
        else:
            arr[sorted_index] = right_arr[right_index]
            right_index = right_index + 1

        sorted_index = sorted_index + 1

   # добавление остатка в конец
    while left_index < len(left_arr):
        arr[sorted_index] = left_arr[left_index]
        left_index = left_index + 1
        sorted_index = sorted_index + 1

    while right_index < len(right_arr):
        arr[sorted_index] = right_arr[right_index]
        right_index = right_index + 1
        sorted_index = sorted_index + 1


# Вариант 2 (Более простой)

def merge_list(a ,b): # Метод слияния 
    temp = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    if i < len(a):    # Заполнение хвоста A и B
        temp += a[i:]
    if j < len(b):
        temp += b[j:]
    return temp 


def merge_sort_lite(arr):   # Главня функцыя сортировки 
    if len(arr) == 1:
        return arr
    midle = len(arr) // 2 
    left = merge_sort_lite(arr[:middle])
    right = merge_sort_lite(arr[midle:])
    return merge_list(left , right)

