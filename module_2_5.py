'''
Наипши функцию get_matrix с тремя параметрами n, m и value, которая будет создавать
матрицу(вложеный список) размерами n строк и m столбцов, заполненную значениями value и возвращать
эту матрицу в качестве результата работы.
'''

# Решение задачи «Матрица воплоти»
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        sublist = []
        for j in range(m):
            sublist.append(value)
        matrix.append(sublist)
    return matrix

result = get_matrix(4, 2, 13)
print(result)
