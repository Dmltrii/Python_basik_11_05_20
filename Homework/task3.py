'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        # print(sum(self.income.values()))


class Position(Worker):

    def get_full_name(self):
        return print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Дохода с учетом премии: {sum(self._income.values())}')


person_1 = Position('Иван', 'Иванов', 'Мастер-фломастер', 122, 123)
person_1.get_full_name()
person_1.get_total_income()
