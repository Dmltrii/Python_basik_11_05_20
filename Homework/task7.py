'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
 методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNum:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return ComplexNum(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other):
        return ComplexNum(self.__x * other.__x - self.__y * other.__y, self.__y * other.__x + other.__y * self.__x)

    def __str__(self):
        return f'{self.__x} + i * {self.__y}'


z1 = ComplexNum(1, 2)
print(z1)
z2 = ComplexNum(2, 1)
print(z2)
z3 = z1 + z2
print(z3)
z4 = z1 * z2
print(z4)