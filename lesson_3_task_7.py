# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random
n = 10
array = [random.randint(0, 20) for x in range(n)]

def two_min(array):
    min_el_1 = array[0]
    for i in array:
        if i < min_el_1:
            min_el_1 = i

    array.remove(min_el_1)

    min_el_2 = array[0]
    for i in array:
        if i < min_el_2:
            min_el_2 = i
    return min_el_1, min_el_2

print(f'initial list: {array}')
print(f'two lowest integers are: {two_min(array)}')