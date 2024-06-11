def Counting_sort(arr , n):
    count = [0]*(n + 1)
    for i in arr:
        count[i] += 1

    otv = ''
    for i in range(n + 1):
        if count[i] > 0:
            otv += ((str(i)+ ' ') * count[i])
    arr = []
    for i in otv:
        if i != ' ':
            arr.append(i)
    return arr


n = int(input())
arr = list(map(int , input().split()))
print(*Counting_sort(arr, n))