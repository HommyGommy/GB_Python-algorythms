# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

n = 20
array = [random.randint(-20, 20) for x in range(n)]

negative_list = [x for x in array if x <0]

max_el = negative_list[0]

for i in negative_list:
    if i > max_el:
        max_el = i


print(f'initial array: {array}')
print(f'max negative element = {max_el}, pos (index) = {array.index(max_el)}')