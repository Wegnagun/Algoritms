def binary_search(lst, num, low, high):
    """ Бинарный поиск через while """
    nums = sorted(lst)
    while low < high:
        mid = (low + high) // 2
        target = nums[mid]
        if target == num:
            return mid
        elif target < num:
            low = mid + 1
        else:
            high = mid
    return 'Нет такого числа'


if __name__ == '__main__':
    first_test = [-33, -1, 1, 3, 4, 5, 6, 7, 8, 13, 14, 22, 22, 99]
    print(binary_search(first_test, num=7, low=0, high=len(first_test)))
