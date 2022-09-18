def recursion_binary_search(lst, num, low, high):
    """ Бинарный поиск через рекурсию """
    if high <= low:
        return 'Нет такого числа'
    mid = (low + high) // 2
    if lst[mid] == num:
        return mid
    elif num < lst[mid]:
        recursion_binary_search(lst, num, low, mid)
    else:
        recursion_binary_search(lst, num, mid + 1, high)


if __name__ == '__main__':
    first_test = [-33, -1, 1, 3, 4, 5, 6, 7, 8, 13, 14, 22, 22, 99]
    second_test = []
    print(
        recursion_binary_search(first_test, num=7, low=0, high=len(first_test))
    )
