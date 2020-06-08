'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print(f'Запуск отрисовки {self.title} канцелярской принадлежности.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручка.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандаша.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркер.')


ai = Stationery('супер')
ai_1 = Pen('супер')
ai_2 = Pencil('супер')
ai_3 = Handle('супер')
