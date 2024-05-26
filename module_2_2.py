'''
Задача "Все ли равны?":
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0
'''

# Решение задачи «Все ли равны?»

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

my_set = {first, second, third}
if len(my_set) == 1:
    print(3)
elif len(my_set) == 2:
    print(2)
else:
    print(0)