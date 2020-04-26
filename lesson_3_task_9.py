# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
"""Создадим random матрицу 5х5"""
matrix = [[random.randint(1,9) for i in range (5)] for i in range (5)]

"""Для наглядности выводим матрицу"""
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

"""Транспонируем матрицу, чтобы удобней было итерироваться по строкам"""
matrix_t = list(zip(*matrix))

"""Создадим пустой список, куда будем добавлять минимумы по каждому столбцу (или строке из транспонированный матрицы)"""
min_el_list = []

"""Добавляем минимальные элементы в новый спислк min_el_list"""
for i, line in enumerate(matrix_t):
    min_el = matrix_t[i][0]
    for item in line:
        if item < min_el:
            min_el = item
    min_el_list.append(min_el)

"""Определяем максимум из списка"""
max_el = min_el_list[0]
for i in min_el_list:
    if i > max_el:
        max_el = i
print('-' * 24)
print(f'max element from column minimums: {max_el}')
