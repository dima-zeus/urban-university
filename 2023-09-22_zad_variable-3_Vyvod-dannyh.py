'''
Задача «Работаем с выводом данных».

Описание: Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.
Формат ввода
название товара;
цена товара;
вес товара;
количество денег у пользователя.

Формат вывода
Чек <название товара> - <вес>кг - <цена>руб/кг Итого: <итоговая стоимость>руб Внесено: <количество денег от пользователя>руб Сдача: <сдача>руб
'''

# Решение задачи «Работаем с выводом данных»
name = input('название товара: ')
price = float(input('цена товара: '))
weight = float(input('вес товара: '))
money = float(input('количество денег: '))
sdacha = money - price * weight

print('Чек')
print(f'{name}')
print(f'Вес: {weight}кг')
print(f'Цена: {price}руб/кг')
print(f'Итого: {price * weight}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {sdacha}руб')
