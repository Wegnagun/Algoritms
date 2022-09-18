import math


def linear_search(lst, num, left, right):
    for item in range(left, right + 1):
        if lst[item] == num:
            return item
    return 'Нет такого числа'


def jump_search(lst, num):
    """ поиск прыжками, уулучшенный линейный поиск. """
    length = len(lst)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lst[left] <= num:
        right = min(length - 1, left + jump)
        if lst[left] <= num <= lst[right]:
            break
        left += jump
    if left >= length or lst[left] > num:
        return 'Нет такого числа'
    right = min(length - 1, right)
    print(f'{left} {right}')
    return linear_search(lst, num, left, right)


if __name__ == '__main__':
    first_test = [-33, -1, 1, 3, 4, 5, 6, 7, 8, 13, 14, 22, 22, 99]
    print(jump_search(first_test, num=0))
