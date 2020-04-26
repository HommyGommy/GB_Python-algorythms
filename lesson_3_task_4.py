# 4. Определить, какое число в массиве встречается чаще всего.
import random
""" Создаим массив случайных чисел"""
n = 10
array = [random.randint(1, 5) for x in range (n)]

max = 0
res = array[0]
for i in array:
    freq = array.count(i)
    if freq > max:
        max = freq
        res = i

print(f'init list: {array}')
print(f'the most frequent int is {res}')