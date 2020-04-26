# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

n = 20
min = 1
max = 100

""" Создаим массив случайных чисел"""
array = [random.randint(min, max) for x in range (n)]

"""Создадим второй массив, в котором будет содержаться ответ (чтобы не изменять начальный)"""
array_new = array.copy()

"""Найдем максимальный и минимальный элементы"""
el_min = el_max = array[0]

for i in array:
    if i > el_max:
        el_max = i
    else:
        if i < el_min:
            el_min = i

"""Добавляем условие, когда индекс el_max может быть > или < индекса el_min"""

if array.index(el_max) > array.index(el_min):
    array_new[array_new.index(el_max)], array_new[array_new.index(el_min)] = array_new[array_new.index(el_min)], array_new[array_new.index(el_max)]
else:
    array_new[array_new.index(el_min)], array_new[array_new.index(el_max)] = array_new[array_new.index(el_max)], array_new[array_new.index(el_min)]

print(f'old list: {array}')
print(f'max el = {el_max}')
print(f'min el = {el_min}')
print(f'new list: {array_new}')
