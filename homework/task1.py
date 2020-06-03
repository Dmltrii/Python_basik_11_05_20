'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
 ввода данных свидетельствует пустая строка.
'''

out_file = open("out_file.txt", "w")
while True:
    str_input = input('Введите строку для записи или нажмите Enter для выхода:\n')
    if str_input:
        out_file.writelines(str_input)
        out_file.writelines('\n')
    else:
        break
out_file.close()
