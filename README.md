# Algoritms
Wegnaguns algoritms library (наполняю по мере наличия времени...)

Решил тут собирать алгоритмы, чтобы не вылетали из головы и закреплять знания по алгоритмам


# Алгоритмы поиска

### Бинарный поиск

`Бинарный поиск ищет в отсортированном массиве.
Сложность алгоритма двоичного поиска в лучшем случае составляет O(1). 
В лучшем случае найдем число с первого раза, а в худшем и среднем сложность 
составляет O(log(n))`

[Бинарный поиск через итерацию](search_algoritms/binary_search.py)  
[Бинарный поиск через рекурсию](search_algoritms/recursion_binary_search.py)  

### Jump поиск

`Поиск в отсортированном массиве, проходимся отрезкам массива и если 
заданное число содержется в отрезке, линейным поиском ищем индекс элемента.
Сложность этого алгоритма составляет О(√n), где √n - размер прыджка, 
а n - длина списка. По эффективности находится между линейным и бинарный 
поиском. Но на больших массивах может быть эффективнее бинарного за счёт 
отказа от использования оператора деления (использование опертора деления 
дороже чем остальные основные операторы за счёт итеративности процедуры)`  

[Jump поиск](search_algoritms/jump_search.py)  
