# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

n = 20
array = [random.randint(-10, 20) for x in range(n)]
res = array.copy()
max_el = min_el = array[0]

for i in array:
    if i > max_el:
        max_el = i
    else:
        if i < min_el:
            min_el = i

res.remove(min_el)
res.remove(max_el)

print(f'initial list: {array}, sum of elements = {sum(array)}')
print(f'min = {min_el} and max ={max_el}')
print(f'sum without min and max = {sum(res)}')