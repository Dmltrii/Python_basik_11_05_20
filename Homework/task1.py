'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def div():
    while True:
        num_a = input('Введите делимое: ')
        try:
            num_a = int(num_a)
        except ValueError:
            print("Не верное значение данных\n")
            continue
        break
    while True:
        num_b = input('Введите делитель: ')
        try:
            num_b = int(num_b)
            result = num_a / num_b
        except ValueError:
            print("Не верное значение данных\n")
            continue
        except ZeroDivisionError:
            print("Делитель не может быть равен 0\n")
            continue
        break
    return result


print(div())
