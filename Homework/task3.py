'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
 и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
'''


class Cell:
    def __init__(self, num_of_cells: int):
        self.__num_of_cells = int(num_of_cells)
        self.__num_of_cells_out = self.__num_of_cells

    def __add__(self, other):
        self.__num_of_cells_out = self.__num_of_cells + other.__num_of_cells
        return Cell(self.__num_of_cells)

    def __sub__(self, other):
        self.__num_of_cells_out = self.__num_of_cells - other.__num_of_cells
        if self.__num_of_cells_out > 0:
            return Cell(self.__num_of_cells_out)
        else:
            return f'Not enough cells'

    def __mul__(self, other):
        self.__num_of_cells_out = self.__num_of_cells * other.__num_of_cells
        return Cell(self.__num_of_cells_out)

    def __truediv__(self, other):
        result = self.__num_of_cells / other.__num_of_cells
        rest = result - int(result)
        # print(result)
        if rest > 0.5:
            self.__num_of_cells_out = int(result + 1)
            return Cell(self.__num_of_cells_out)
        else:
            self.__num_of_cells_out = int(result)
            return Cell(self.__num_of_cells_out)

    def make_order(self, order: int):
        result = ''
        order = int(order)
        rest = self.__num_of_cells % order
        num_of_rows = self.__num_of_cells // order
        for _ in range(num_of_rows):
            result += '*' * order + '\\n'
        result += '*' * rest
        return result

    def __str__(self):
        return f'{self.__num_of_cells}'


one = Cell(7)
two = Cell(2)

res = one + two
print(res)
res = one - two
print(res)
res = one * two
print(res)
res = one / two
print(res)
print(res.make_order(3))
