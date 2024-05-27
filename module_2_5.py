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
