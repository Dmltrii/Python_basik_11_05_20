'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:

    def __init__(self, list_of_lists: list):
        self.__list_of_lists = list(list_of_lists)

    def __str__(self):
        len_num_max = 0
        for line in self.__list_of_lists:
            for num in line:
                len_num = len(str(num))
                if len_num_max < len_num:
                    len_num_max = len_num
        result = ''
        for i in self.__list_of_lists:
            result += (' '.join(f'{num:<{len_num_max}}' for num in i)) + '\n'
        return result

    def __add__(self, other):
        result = []
        for line_x, line_y in zip(self.__list_of_lists, other.__list_of_lists):
            result.append(list(map(sum, zip(line_x, line_y))))
        return Matrix(result)


matrix_1 = Matrix([[1, 200, 3], [1111111111, 2, 3], [1, 2, 3]])
matrix_2 = Matrix([[1, 200, 3], [1, 2, 3], [1, 2, 3]])
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
