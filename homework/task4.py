'''
4. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

import functools

def mux(el_prev, el):
    return el_prev * el

my_list = [el for el in range(99, 1001) if el % 2 == 0]
mux = functools.reduce(mux, my_list)
print(my_list)
print(mux)