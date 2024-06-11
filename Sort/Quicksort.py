
def Quicksort (arr):

    if len(arr)<= 1:
        return arr

    osn_el = arr[-1]

    left = list(filter(lambda x: x < osn_el, arr))
    centre = [i for i in arr if i == osn_el]
    right = list(filter(lambda x: x > osn_el, arr))
    
    return Quicksort(left) + centre + Quicksort(right)

arr = list(map(int, input().split()))
print(Quicksort(arr))