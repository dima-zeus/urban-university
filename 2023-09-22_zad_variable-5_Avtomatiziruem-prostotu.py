'''
Задача «Автоматизируем простоту!».
Описание:
Формат ввода
В первой строке записано одно натуральное число ? Во второй строке записано любимое дело.
Формат вывода
? строк вида: Обожаю писать "<любимое дело>"!
'''

# Решение задачи «Автоматизируем простоту!»
n = int(input('Одно натуральное число: '))
favorite_case = input('Любимое дело: ')
print(f'Обожаю писать "{favorite_case}"!\n' * n)
