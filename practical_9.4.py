# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, \
#                                                                                остановилась, повернула (куда);

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'car {self.name} go, color {self.color}'

    def stop(self):
        return f'car {self.name} stop'

    def turn(self, direction):
        return f'car {self.name} to turn {direction}'

    def show_speed(self):
        return f'car {self.name} have speed {self.speed}'


# # опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'car {self.name} wowowo exceeds by {self.speed - 60}'
        else:
            return f'car {self.name} speed {self.speed}'


class SportCar(Car):
    def show_speed(self):
        if self.speed < 200:
            return f'Are you sure a sports car?'



class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'car {self.name} wowowo exceeds by {self.speed - 60}'
        else:
            return f'car {self.name} speed {self.speed}'


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car_1 = TownCar('MAN', 90, 'Blue')
    car_2 = SportCar('BMW', 199, 'Blue - red - yellow')
    car_3 = WorkCar('Reno', 90, 'Green')
    car_4 = PoliceCar('Ford', 110, 'Black')
    print(car_1.go(), car_1.turn('Left'), car_1.show_speed(), car_1.stop())
    print(car_2.go(), car_2.turn('Right'), car_2.show_speed(), car_2.stop())
    print(car_3.go(), car_3.turn('Left'), car_3.show_speed(), car_3.stop())
    print(car_4.go(), car_4.turn('Left'), car_4.show_speed(), car_4.stop())