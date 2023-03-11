#skończone
from copy import deepcopy


class Matrix:

    def __init__(self, obj, fill=0) -> None:
        if isinstance(obj, tuple):
            n, m = obj
            self.matrix = n*[fill]
            for i in range(n):
                self.matrix[i] = m*[fill]
        else:
            self.matrix = deepcopy(obj)


    def size(self):
        if len(self.matrix):
            return len(self.matrix), len(self.matrix[0])
        else:
            return 0, 0

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.size() == other.size():
            n, m = self.size()
            new_matrix = Matrix((n, m))
            for i in range(n):
                for j in range(m):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
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
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    new_matrix[i][j] = sum
            return new_matrix
        else:
            raise Exception("Zły wymiar macierzy")


    def __setitem__(self, key, item):
        self.matrix[key] = item
    

    def __str__(self):
        str_rep = ''
        for row in self.matrix:
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



def chio(matrix: Matrix):
    if matrix.size()[0] != matrix.size()[1]:
        return 'brak wyznacznika'
    if matrix.size()[0] == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    #podmiana wiersza z pierwszym niezerowym elementem, domnożenie -1 bo zmiana wierszy wyznacznika
    swapped = 1
    if matrix[0][0] == 0:
        for idx, row in enumerate(matrix[1:], 1):
            if row[0] != 0:
                matrix[0], matrix[idx] = matrix[idx], matrix[0]
                swapped *= -1
                break
    n = matrix.size()[0]
    new_matrix = Matrix((n-1,n-1))
    for i in range(n-1):
        for j in range(n-1):
            new_matrix[i][j] = matrix[0][0]*matrix[i+1][j+1] - matrix[i+1][0]*matrix[0][j+1]
    return swapped*1/matrix[0][0]**(matrix.size()[0]-2) * (chio(new_matrix))


if __name__ == '__main__':
    mt = Matrix([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
    print(chio(mt))
    mt = Matrix([
    
    [5 , 1 , 1 , 2 , 3],
    
    [4 , 2 , 1 , 7 , 3],
    
    [2 , 1 , 2 , 4 , 7],
    
    [9 , 1 , 0 , 7 , 0],
    
    [1 , 4 , 7 , 2 , 2]
    
    ])
    print(chio(mt))
