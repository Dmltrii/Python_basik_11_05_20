#Task1
var_input_num = input('Введите число: ')

while not (int(var_input_num.isdigit())):
    print('Не коректный ввод')
    var_input_num = input('Введите число: ')

var_input_str = input('Введите фразу: ')

while int(var_input_str.isdigit()):
    print('Не коректный ввод')
    var_input_str = input('Введите фразу: ')

print('\nВаше число:\n',var_input_num)
print('Ваша фраза:\n',var_input_str)
