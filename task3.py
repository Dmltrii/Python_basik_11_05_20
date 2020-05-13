# Task3

num_n = input('Введите число n: ')

while not (int(num_n.isdigit())):
    print('Не коректный ввод')
    num_n = input('Введите число n: ')

num_n_int = int(num_n)
num_nn_int = int(num_n + num_n)
num_nnn_int = int(num_n + num_n + num_n)
num_sum = num_n_int + num_nn_int + num_nnn_int
print(f'n + nn + nnn = {num_sum}')
