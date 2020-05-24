'''
5. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые числа,
начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
'''

# 5a


from itertools import count
from sys import argv
# param[0] - старт, param[1] - финиш
param = []
i = 1
while i < 3:
    if argv[i].isdigit():
        param.append(int(argv[i]))
    else:
        print('Неверный ввод ')
    i += 1

for i in count(param[0]):
    if i > param[1]:
        break
    else:
        print(i)



# 5b


from itertools import cycle
from sys import argv
# param[0] - строка, param[1] - количество итераций
param = []
param.append(argv[1])
if argv[2].isdigit():
    param.append(int(argv[2]))
else:
    print('Неверный ввод ')
i = 0

for el in cycle(param[0]):
    if i > param[1]:
        break
    else:
        print(el)
    i += 1
