def Prefix(text):
    n = len(text)
    arr = [0] * n
    for i in range(1 , n):
        j = arr[i - 1]
        while j > 0 and text[j] != text[i]:
            j = arr[j-1]
        if text[i] == text[j]:
            j+=1
        arr[i] = j
    return arr

text = input()

print(*Prefix(text))