'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
 который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
  В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
   уникальные для каждого типа оргтехники.
'''

'''
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу 
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также 
других данных, можно использовать любую подходящую структуру, например словарь.
'''

'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных 
на уроках по ООП.
'''


class Storeage:
    __dicter = []

    def set_store(self, in_dicter: dict):
        self.__dicter.append([in_dicter])

    def __str__(self):
        return f'{self.__dicter}'


class OfficeEquipment:

    def __init__(self, name, id_num, quantity, price):
        self.__name = name
        self.__id_num = id_num
        self.__quantity = quantity
        self.__price = price
        # return {'name': self.__name, 'ind': self.__ind,'quantity': self.__quantity,'price': self.__price}

    def get_unit(self):
        return {'name': self.__name, 'ind': self.__id_num, 'quantity': self.__quantity, 'price': self.__price}

    def set_unit(self, name, id_num, quantity, price):
        self.__name = name
        if id_num.isdigit():
            self.__id_num = int(id_num)
        else:
            print('Ошибка ввода')

        if price.isdigit():
            self.__price = int(price)
        else:
            print('Ошибка ввода')

        if quantity.isdigit():
            self.__quantity = int(quantity)
        else:
            print('Ошибка ввода')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


unit1 = Printer('La_print', 123, 122, 123)
unit2 = Scanner('La_scan', 123, 122, 123)
unit3 = Xerox('La_copy', 123, 122, 123)

store = Storeage()
store.set_store(unit1.get_unit())
store.set_store(unit2.get_unit())
store.set_store(unit3.get_unit())

print(store)