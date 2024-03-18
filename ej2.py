def determinant_recursive(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        sign = (-1) ** i
        minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
        det += sign * matrix[0][i] * determinant_recursive(minor)

    return det


def determinant_iterative(matrix):
    det = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    return det


# Ejemplo de matriz 3x3
matrix = [[2, 3, 1], [5, 4, 6], [7, 8, 9]]

# Calculando el determinante utilizando el método recursivo
det_recursive = determinant_recursive(matrix)
print("Determinante (Recursivo):", det_recursive)

# Calculando el determinante utilizando el método iterativo
det_iterative = determinant_iterative(matrix)
print("Determinante (Iterativo):", det_iterative)


