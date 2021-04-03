class Cell:
    def __init__(self, par):
        self.par = par

    def __add__(self, other):
        return Cell(self.par + other.par)

    def __sub__(self, other):
        if self.par > other.par:
            return Cell(self.par - other.par)
        else:
            raise ValueError('Subtraction operation cannot be performed')

    def __mul__(self, other):
        return Cell(self.par * other.par)

    def __floordiv__(self, other):
        if other.par != 0:
            return Cell(self.par // other.par)
        else:
            raise ZeroDivisionError('integer division or modulo by zero   OWOWOWOW')

    def make_order(self, rows):
        list_comper = ['*' * rows + '\n' for _ in range(self.par // rows)]
        list_comper.append('*' * (self.par % rows))
        return ''.join(list_comper)

    def __str__(self):
        return '*' * self.par


if __name__ == '__main__':
    try:
        cell_1 = Cell(8)
        cell_2 = Cell(4)
        print(cell_1 + cell_2 - cell_1)
        print(cell_1 - cell_2 + cell_1)
        print(cell_1 * cell_2)
        print()
        print(cell_1 // cell_2)
        print()
        print(cell_1.make_order(3))
    except (ValueError, ZeroDivisionError) as err:
        print(err)
    else:
        print('All good!')
    finally:
        print('life is Beautiful')