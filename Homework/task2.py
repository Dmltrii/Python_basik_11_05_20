'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Cloths(ABC):

    @property
    @abstractmethod
    def material_quantity(self):
        pass


class Coat(Cloths):

    def __init__(self, name, v_size):
        self.__name = name
        self.__v_size = v_size

    @property
    def material_quantity(self):
        return f'{self.__name} требует  {self.__v_size / 6.5 + 0.5} ткани'


class Suit(Cloths):

    def __init__(self, name, h_size):
        self.__name = name
        self.__h_size = h_size

    @property
    def material_quantity(self):
        return f'{self.__name} требует  {2 * self.__h_size + 0.3} ткани'


trench = Coat('Укполтетк', 123)
hugo = Suit('Костюмишку', 123)
print(trench.material_quantity)
print(hugo.material_quantity)
