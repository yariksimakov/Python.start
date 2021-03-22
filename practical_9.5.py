# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        return f'Start rendering {self.name}'


class Pen(Stationery):
    def draw(self):
        return f'{self.name} painted by pen'



class Pencil(Stationery):
    def draw(self):
        return f'{self.name} painted by pencil'


class Handle(Stationery):
    def draw(self):
        return f'{self.name} painted by handle'


if __name__ == '__main__':
    start = Stationery('Picture')
    print(start.name)
    print(start.draw())
    start = Pen('Picture')
    print(start.draw())
    start = Pencil('Picture')
    print(start.draw())
    start = Handle('Picture')
    print(start.draw())