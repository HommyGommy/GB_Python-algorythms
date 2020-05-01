# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""Мой вариант"""

import cProfile
def range_change(n):
    import random
    array = [random.randint(-100, 100) for x in range (n)]
    el_min = el_max = array[0]

    for i in array:
     if i > el_max:
         el_max = i
     else:
         if i < el_min:
             el_min = i

    if array.index(el_max) > array.index(el_min):
     array[array.index(el_max)], array[array.index(el_min)] = array[array.index(el_min)], array[array.index(el_max)]
    else:
     array[array.index(el_min)], array[array.index(el_max)] = array[array.index(el_max)], array[array.index(el_min)]

    return f'new list {array}'

cProfile.run('range_change(1000)')


# "lesson_4_task_1.range_change(10)"
# 1000 loops, best of 5: 11.1 usec per loop

# "lesson_4_task_1.range_change(100)"
# 1000 loops, best of 5: 91.3 usec per loop

# "lesson_4_task_1.range_change(1000)"
# 1000 loops, best of 5: 879 usec per loop

# cProfile.run('range_change(10)')
# 1685 function calls (1647 primitive calls) in 0.004 seconds

# cProfile.run('range_change(100)')
# 2148 function calls (2110 primitive calls) in 0.004 seconds

# cProfile.run('range_change(1000)')
# 6888 function calls (6850 primitive calls) in 0.009 seconds

"""Вариант решения с урока"""

def range_change(n):
    import random
    array = [random.randint(-100, 100) for x in range (n)]
    idx_min = 0
    idx_max = 0
    for i in range(n):
     if array[i] < array[idx_min]:
         idx_min = i
     elif array[i] > array[idx_max]:
         idx_max = i
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return f'new list: {array}'

cProfile.run('range_change(1000)')
# "lesson_4_task_2.range_change(10)"
# 1000 loops, best of 5: 10.8 usec per loop

# "lesson_4_task_2.range_change(100)"
# 1000 loops, best of 5: 92.9 usec per loop

# "lesson_4_task_2.range_change(1000)"
# 1000 loops, best of 5: 945 usec per loop

# cProfile.run('range_change(10)')
# 1677 function calls (1639 primitive calls) in 0.005 seconds

# cProfile.run('range_change(100)')
# 2151 function calls (2113 primitive calls) in 0.004 seconds

# cProfile.run('range_change(1000)')
# 6897 function calls (6859 primitive calls) in 0.008 seconds

"""Вариант решения с урока с использованием min/max"""
def range_change(n):
    import random
    array = [random.randint(-100, 100) for x in range (n)]
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return f'new list: {array}'

cProfile.run('range_change(1000)')
# "lesson_4_task_3.range_change(10)"
# 1000 loops, best of 5: 10.7 usec per loop

# "lesson_4_task_3.range_change(100)"
# 1000 loops, best of 5: 89.8 usec per loop

# "lesson_4_task_3.range_change(1000)"
# 1000 loops, best of 5: 882 usec per loop

# cProfile.run('range_change(10)')
# 1686 function calls (1648 primitive calls) in 0.004 seconds

# cProfile.run('range_change(100)')
# 2150 function calls (2112 primitive calls) in 0.004 seconds

# cProfile.run('range_change(1000)')
# 6878 function calls (6840 primitive calls) in 0.007 seconds

"""Общий вывод: предлагаю использовать мой вариант, т.к. в timeit на больших n работает быстрее, а разница между кол-м вызываемых функций в cProfile незначительна"""





