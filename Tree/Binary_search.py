def Binary_serch(larr, elenet):
    larr = sort()
    os_element = len(larr) // 2
    res = -1
    len_arr = len(larr)
    while True:
        if len_arr == 1:
            res = larr[0]
            break
        if larr[os_element] < elenet:
            larr = larr[os_element:]
        elif larr[os_element] > elenet:
            larr = larr[:os_element]
        else:
            res = larr[os_element]
            break
        len_arr = len(larr)
        os_element = len_arr // 2
    return res