from binary_search import binary_search


def galloping_search(lst, num):
    """ Экспоненциальный поиск """
    if lst[0] == num:
        return 0
    index = 1
    while index < len(lst) and lst[index] <= num:
        index = index * 2
    return binary_search(lst, num, 0, min(index, len(lst)))


if __name__ == '__main__':
    first_test = [-33, -1, 1, 3, 4, 5, 6, 7, 8, 13, 14, 22, 22, 99]
    print(galloping_search(first_test, num=7))
