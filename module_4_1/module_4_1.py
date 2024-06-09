'''
В школе нам говорили, что на 0 делить нельзя. Высшая же математика опровергает это и говорит, что результат при делении
на 0 будет стремиться к бесконечности.
Давайте реализуем оба способа, чтобы у вас всегда был выбор!
Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
В fake_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат
деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат
деления first на second, но когда в second записан 0 - возвращать бесконечность.
Бесконечность можно импортировать из встренной библиотеки math (from math import inf)
'''

# Решение задачи "А как делить?"

from fake_math import divide as fdivide
from true_math import divide as tdivide


if __name__ == '__main__':
    result1 = fdivide(69, 3)
    result2 = fdivide(3, 0)
    result3 = tdivide(49, 7)
    result4 = tdivide(15, 0)
    print(result1)
    print(result2)
    print(result3)
    print(result4)

