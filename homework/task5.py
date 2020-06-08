'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import os
import random

line_list = []
file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')
list_of_numbers = [el * random.randrange(2, 10, 3) for el in range(10, 20)]
print(list_of_numbers)
print(sum(map(int, list_of_numbers)))
with open(file_path, 'w', encoding='UTF-8') as out_file:
    for _ in list_of_numbers:
        out_file.writelines(str(_))
        out_file.writelines(' ')
with open(file_path, 'r', encoding='UTF-8') as in_file:
    line_list = in_file.readline()
    sum = sum(map(int, line_list.split()))
print(sum)
