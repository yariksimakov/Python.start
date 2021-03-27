from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        """
        Если вы задаётесь вопросом зачем сдесь zip_longest() то это чтобы вслучае если по
        по правилам математики матрицы нельзя складывать то программа выдовала ошибку
        """
        return Matrix([
            [el_1 + el_2 for el_1, el_2 in zip_longest(row_1, row_2)]
            for row_1, row_2 in zip_longest(self.matrix, other.matrix)
        ])

    def __str__(self):
        return f'{self.matrix}'.replace(",", "").replace("] [", "\n").replace("[", '').replace("]", '')


if __name__ == '__main__':
    mat_1 = Matrix([[1, 2, 3], [3, 4, 7]])
    mat_2 = Matrix([[1, 2, 3], [5, 6, 8]])
    try:
        print(mat_1 + mat_2 + mat_1)
    except TypeError:
        print('matrix data cannot be added')