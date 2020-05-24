'''Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.'''

def my_func(x, y) -> float:
    result = 1
    while y < 0:
        result = (1 / x) * result
        y += 1

    return result


def my_func0(x, y) -> float:
    result = x ** y

    return result

while True:
    num_x = input('Введите действительное положительное число x: ')
    try:
        num_x = float(num_x)
    except ValueError:
        print("Не верное значение данных\n")
        continue
    if num_x < 0:
        print("Не верное значение данных\n")
        continue
    break

while True:
    num_y = input('Введите целое отрицательное число y: ')
    try:
        num_y = int(num_y)
    except ValueError:
        print("Не верное значение данных\n")
        continue
    if num_y > 0:
        print("Не верное значение данных\n")
        continue
    break





print(my_func(num_x, num_y))
print(my_func0(num_x, num_y))
