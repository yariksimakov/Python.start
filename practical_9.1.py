from time import sleep
from itertools import cycle

# green, yellow, red

class TrafficLight:
    def __init__(self, *args):
        if args[0].lower() != 'red' or args[1].lower() != 'yellow' or args[2].lower() != 'green':
            raise ValueError('incorrect sequence of input data')
        self.__color = args

    def start_color(self):
        for el in cycle(self.__color):
            print(el)
            if el.lower() == 'green':
                sleep(4)
            elif el.lower() == 'yellow':
                sleep(2)
            elif el.lower() == 'red':
                sleep(7)
            else:
                raise ValueError(f'no such color - {el}')


if __name__ == '__main__':
    try:
        TrafficLight('red', 'yellow', 'green').start_color()
    except ValueError as err:
        print(err)
