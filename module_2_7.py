'''
Напиши функцию get_multiplied_digits, которая принимает аргумент целое чиcло number и подсчитывает произведение цифр этого числа.
'''

# Решение задачи «Рекурсивное умножение цифр»

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[:1])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number

result = get_multiplied_digits(40203)
print(result)
