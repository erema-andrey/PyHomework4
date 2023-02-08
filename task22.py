# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите кол-во элементов в первом множеcтве: '))
m = int(input('Введите кол-во элементов во втором множеcтве: '))
set_first = set()
set_second = set()
i = 0
y = 0
limit = 15
while i < n:
    x = random.randrange(limit)
    set_first.add(x)
    i += 1
while y < n:
    z = random.randrange(limit)
    set_second.add(z)
    y += 1

print(*sorted(list(set(set_first) & set(set_second))))

