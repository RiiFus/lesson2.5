def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix
result = get_matrix(4, 2, 20)
print(result)
