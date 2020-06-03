'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
import os
# list = []
# list.append('One')
# print(list[0] == 'One')


file_path = os.path.join(os.path.dirname(__file__), 'out_task4.txt')
line_list = []
with open("to_task4", encoding='utf-8') as in_file:
    for line in in_file:
        line_list.append(line.split())


for line in line_list:
    for _ in line:

        if line[0] == 'One':
            line[0] = 'Один'
        elif line[0] == 'Two':
            line[0] = 'Два'
        elif line[0] == 'Three':
            line[0] = 'Три'
        elif line[0] == 'Four':
            line[0] = 'Четыре'


with open(file_path, 'w', encoding='UTF-8') as out_file:
    for line in line_list:
        out_file.writelines(' '.join(line))
        out_file.writelines('\n')