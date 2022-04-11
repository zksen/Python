class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        add_matrix = []
        str_1 = "Матрицы должны быть равноразмерными!"
        str_2 = "Это должны быть матрицы!"
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                add_matrix.append([0 for el in self.matrix[i]])
                if len(self.matrix[i]) == len(other.matrix[i]):
                    for j in range(len(self.matrix[i])):
                        if len(self.matrix) == len(self.matrix[i]) and len(other.matrix) == len(other.matrix[i]):
                            add_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                        else:
                            return str_2
                else:
                    return str_1
            return Matrix(add_matrix)
        else:
            return str_1


my_matrix_1 = Matrix([[1, 2, 3], [2, 4, 6], [5, 10, 15]])
my_matrix_2 = Matrix([[3, 6, 9], [4, 8, 12], [6, 12, 18]])

print(my_matrix_1 + my_matrix_2)
