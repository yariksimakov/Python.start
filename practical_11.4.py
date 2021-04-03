class WarehouseDescription:
    data = {}

    def __init__(self, **kwargs):

        try:
            Orchard.chek_data(kwargs)
        except ValueError as err:
            print(err)
        else:
            for el_key in kwargs.keys():
                """ Теперь можно не только хранить но и добавлять в склад"""
                if el_key not in WarehouseDescription.data:
                    WarehouseDescription.data[el_key] = kwargs[el_key]
                else:
                    WarehouseDescription.data[el_key] += kwargs[el_key]
            print(WarehouseDescription.data)


class Orchard:

    @staticmethod
    def to_push(p, s, x):
        WarehouseDescription(printer=p, scanner=s, xerox=x)

    @staticmethod
    def chek_data(el):
        for i in el.values():
            if not isinstance(i, int):
                raise ValueError(f"The entered data is incorrect {i}")


class Printer(Orchard):
    def __init__(self):
        count = WarehouseDescription.data['printer']
        print('{} - printer'.format(count))

    @staticmethod
    def to_push(el):
        WarehouseDescription(printer=el)


class Scanner(Orchard):
    def __init__(self):
        count = WarehouseDescription.data['scanner']
        print('{} - scanner'.format(count))

    @staticmethod
    def to_push(el):
        WarehouseDescription(scanner=el)


class Xerox(Orchard):
    def __init__(self):
        count = WarehouseDescription.data['xerox']
        print('{} - scanner'.format(count))

    @staticmethod
    def to_push(el):
        WarehouseDescription(xerox=el)


if __name__ == '__main__':
    Orchard.to_push(43, 12, 74)
    Printer.to_push(5)
    Printer()
    Scanner.to_push(8)
    Scanner()
    Xerox.to_push(6)
    Xerox()
