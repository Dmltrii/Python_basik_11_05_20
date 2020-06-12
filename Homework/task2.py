'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
  ситуацию и не завершиться с ошибкой.
'''


class Div(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = 10 / 0

except:

    raise Div("Вы ввели отрицательное число!")

else:
    print(f"Все хорошо. Ваш ответ: {a}")

#
#
# class DivisionByNull:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Деление на ноль недопустимо")
#
#
# div = DivisionByNull(10, 100)
# print(DivisionByNull.divide_by_null(10, 0))
# print(DivisionByNull.divide_by_null(10, 0.1))
# print(div.divide_by_null(100, 0))
