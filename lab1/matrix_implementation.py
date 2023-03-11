#skończone

from copy import deepcopy


class Matrix:

    def __init__(self, obj, fill=0) -> None:
        if isinstance(obj, tuple):
            n, m = obj
            self.__matrix = n*[fill]
            for i in range(n):
                self.__matrix[i] = m*[fill]
        else:
            self.__matrix = deepcopy(obj)


    def size(self):
        if len(self.__matrix):
            return len(self.__matrix), len(self.__matrix[0])
        else:
            return 0, 0

    def __getitem__(self, item):
        return self.__matrix[item]

    def __add__(self, other):
        if self.size() == other.size():
            n, m = self.size()
            new_matrix = Matrix((n, m))
            for i in range(n):
                for j in range(m):
                    new_matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
            return new_matrix
        else:
            raise Exception("Zły wymiar macierzy")


    def __mul__(self, other):
        n, m = self.size()
        r, c = other.size()

        if m == r:
            new_matrix = Matrix((n,c))
            for i in range(n):
                for j in range(c):
                    sum = 0
                    for k in range(m):
                        sum += self.__matrix[i][k] * other.__matrix[k][j]
                    new_matrix[i][j] = sum
            return new_matrix
        else:
            raise Exception("Zły wymiar macierzy")



    def __str__(self):
        str_rep = ''
        for row in self.__matrix:
            str_rep += '| '
            for elem in row[:-1]:
                str_rep += f'{elem}   '
            str_rep += f'{row[-1]} |\n'
        return str_rep


def transpose(matrix: Matrix) -> Matrix:
    n, m = matrix.size()
    new_matrix = Matrix((m, n))
    for i in range(n):
        for j in range(m):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix


if __name__ == '__main__':
    matrix1 = Matrix([[1,0,2], [-1,3,1]])
    print(transpose(matrix1))
    ones = Matrix((2,3), 1)
    print(matrix1 + ones)
    matrix2 = Matrix([[3,1],[2,1],[1,0]])
    print(matrix1 * matrix2)
