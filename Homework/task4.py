'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed: int, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Еду вперед')

    def stop(self):
        print('Останавилась')

    def turn_direction(self, direction):
        print(f'Еду {direction}')

    def show_speed(self):
        print(f'Моя скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Моя скорость выше допустимой и составлияет {self.speed}')
        else:
            print(f'Моя скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(TownCar):
    pass


class PoliceCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


ford = WorkCar(60, 'red', 'ford', True)
ford.show_speed()
ford.go()
ford.turn_direction('влево')
tesla = TownCar(120, 'silver', 'tesla', True)
tesla.show_speed()
lada = PoliceCar(610, 'red', 'ford', True)
lada.show_speed()
