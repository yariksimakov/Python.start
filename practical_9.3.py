# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и
# «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worke:
    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worke):
    def get_full_name(self):
        return f'Employee: {self.name} {self.surname}'

    def get_total_income(self):
        return f'wage: {self._income["wage"]} bonus: {self._income["bonus"]}'


if __name__ == '__main__':
    person_1 = Position('Petr', 'Petrovich', 'manager', wage=150500, bonus=90400)
    print(person_1.get_full_name())
    print(person_1.get_total_income())
