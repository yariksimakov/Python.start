# class Clothes:
# Это я баловался
#     def __init__(self, param, typ):
#         self.typ = typ
#         if typ.lower() == 'coat':
#             self.param = param / 6.5 + 0.5
#         elif typ.lower() == 'costume':
#             self.param = param * 2 + 0.3
#         else:
#             raise ValueError('no type')
#
#     def __str__(self):
#         if self.typ.lower() == 'coat':
#             return f'coat {self.param}'
#         elif self.typ.lower() == 'costume':
#             return f'costumer {self.param}'
#
#     def __add__(self, other):
#         return self.param + other.param
#
#
# if __name__ == '__main__':
#     ob_1 = Clothes(13, 'coat')
#     ob_2 = Clothes(12, 'costume')
#     print(ob_1)
#     print(ob_2)
#     print(ob_1 + ob_2)

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, coat, costume):
        self.par_1 = coat / 6.5 + 0.5
        self.par_2 = costume * 2 + 0.3

    @abstractmethod
    def consumption_cloth(self):
        pass

    @property
    def coat(self):
        return f'Coat fabric consumption {self.par_1}'

    @property
    def costume(self):
        return f'Costume fabric consumption {self.par_2}'


class Sum_cloth(Clothes):
    @property
    def consumption_cloth(self):
        return f'Total tissue consumption {self.par_1 + self.par_2}'


if __name__ == '__main__':
    start = Sum_cloth(26, 6)
    print(start.consumption_cloth)
    print(start.coat)
    print(start.costume)