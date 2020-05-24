'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов'''


def my_func(num_a, num_b, num_c):
    if num_b > num_a:
        num_a, num_b = num_b, num_a
    if num_c > num_b:
        num_b, num_c = num_c, num_b
    # if num_b > num_a:
    #     num_a, num_b = num_b, num_a
    sum = num_a + num_b
    return sum


while True:
    a = input('Введите первое число: ')
    try:
        a = int(a)
    except ValueError:
        print("Не верное значение данных\n")
        continue
    break
while True:
    b = input('Введите второе число: ')
    try:
        b = int(b)
    except ValueError:
        print("Не верное значение данных\n")
        continue
    break
while True:
    c = input('Введите третье число: ')
    try:
        c = int(c)
    except ValueError:
        print("Не верное значение данных\n")
        continue
    break

print(my_func(a, b, c))
