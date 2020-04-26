# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

import random

even = list()
odds = list()

array = [i for i in range(2,100)]

print(f'ans 1 = there are {len([x for x in array if x % 2 == 0])} divisible by 2')
print(f'ans 2 = there are {len([x for x in array if x % 3 == 0])} divisible by 3')
print(f'ans 3 = there are {len([x for x in array if x % 4 == 0])} divisible by 4')
print(f'ans 4 = there are {len([x for x in array if x % 5 == 0])} divisible by 5')
print(f'ans 5 = there are {len([x for x in array if x % 6 == 0])} divisible by 6')
print(f'ans 6 = there are {len([x for x in array if x % 7 == 0])} divisible by 7')
print(f'ans 7 = there are {len([x for x in array if x % 8 == 0])} divisible by 8')
print(f'ans 8 = there are {len([x for x in array if x % 9 == 0])} divisible by 9')


