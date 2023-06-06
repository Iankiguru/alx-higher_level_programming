def remove_char_at(string, n):
    list1 = list(string)
    for j in range(n, len(list1) - 1):
        list1[j] = list1[j + 1]
    list1.pop()
    return ''.join(list1)

