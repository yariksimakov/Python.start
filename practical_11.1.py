class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parsing_info(cls, data):
        d, m, y = (int(el) for el in data.split('-'))
        return cls(d, m, y)

    @staticmethod
    def chek_info(obj):
        if obj.month == 2:
            if obj.day > 28:
                raise ValueError(f'The day in February is incorrectly entered: {obj.day}')
        if (31 < obj.day or obj.day < 0) or (12 < obj.month or obj.month < 0) or (6666 < obj.year):
            raise ValueError(f'Date entered incorrectly: {obj.day}-{obj.month}-{obj.year}')


work_str = '02-02-2021'
if __name__ == '__main__':
    one = Data.parsing_info(work_str)
    try:
        Data.chek_info(one)
    except ValueError as err:
        print(err)
    else:
        print(f'This good date: {work_str}')
