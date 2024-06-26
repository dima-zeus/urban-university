'''
Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
'''

# Решение задачи «Неизменяемые и изменяемые объекты. Кортежи и списки»
immutable_var = ('1', 2, True, [4, 5, '6'])
print(immutable_var)
#immutable_var[1] = 3

mutable_list = [1, '2', 'three']
print(mutable_list)
mutable_list[1:2] = 'two', 'five'
print(mutable_list)