'''
Задача «Сложная сдача».
Описание: Одна из задач, в которой лучше исключить человеческий фактор, — подсчёт сдачи. Определите, какую сдачу нужно
выдать тому, кто купил 4,5кг черешни по цене 34 руб/кг
'''

# Решение задачи «Сложная сдача»
m_cherry = 4.5
price = 34
money_client = input('Принято от покупателя (X.Y), руб.: ')
rub = int(float(money_client))
kop = money_client.split('.')[1]
print(f'Получено: {rub} руб. {kop} коп.')
sdacha = float(money_client) - m_cherry * price
print(f'Вернуть покупателю (X.Y), руб.: {sdacha:.2f}')
