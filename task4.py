# Task4

num_n = input('Введите целое положительное число: ')
while not (int(num_n.isdigit())):
    print('Не коректный ввод')
    num_n = input('Введите целое положительное число: ')

num_n_int = int(num_n)
greatest_number = 0
while num_n_int > 0:
    inst_dig = (num_n_int % 10)
    if inst_dig > greatest_number:
        greatest_number = inst_dig
    num_n_int = num_n_int // 10
print(f'Самая большая цифра в числе равна {greatest_number}')
