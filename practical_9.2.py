class Road:
    def __init__(self, length, width):
        if (type(length) == float or type(length) == int) and (type(width) == float or type(width) == int):
            self._length = length
            self._width = width
        else:
            raise ValueError('Type arguments should be int or float')

    def mass(self):
        return self._length * self._width * 25 * 5


if __name__ == '__main__':
    try:
        print(Road(24.32, 8).mass(), 'ton')
    except (ValueError, TypeError) as err:
        print(f'You are problem {err} and should be two')
