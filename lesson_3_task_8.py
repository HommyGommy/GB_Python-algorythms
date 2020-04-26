# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random
"""Создадим пустую матрицу 4х4"""
matrix = [[0 for i in range (4)] for i in range (4)]

"""Запрашиаем построчно заполнение каждого элемента"""
for i, line in enumerate(matrix):
    for j, item in enumerate(line):
        matrix[i][j] = int(input(f'enter num for line# {i+1} column# {j+1}: '))
    print(f'     sum of elements in line# {i+1}: {sum(matrix[i])} \n')

print('your matrix looks like this: \n')

"""Выводим финальную матрицу и сумму элементов каждой строки"""
for line in matrix:
    sum_line = 0
    for item in line:
        sum_line += item
        print(f'{item:>4}', end='')
    print(f'    | {sum_line}')