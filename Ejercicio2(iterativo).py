class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def determinant_recursive(self):
        if len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        det = 0
        for i in range(len(self.matrix)):
            sign = (-1) ** i
            minor = [row[:i] + row[i + 1:] for row in self.matrix[1:]]
            det += sign * self.matrix[0][i] * Matrix(minor).determinant_recursive()

        return det

    def determinant_iterative(self):
        det = (
            self.matrix[0][0] * (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1])
            - self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0])
            + self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])
        )
        return det


# Ejemplo de matriz 3x3
matrix = [[2, 3, 1], [5, 4, 6], [7, 8, 9]]

# Creando una instancia de la clase Matrix
matrix_obj = Matrix(matrix)


# Calculando el determinante utilizando el método iterativo
det_iterative = matrix_obj.determinant_iterative()
print("Determinante (Iterativo):", det_iterative)



