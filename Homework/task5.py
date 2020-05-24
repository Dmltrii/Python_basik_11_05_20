'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
 сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''


def check_list(num_of_list: list) -> bool:
    for num in num_of_list:
        if num == 'X':
            continue
        else:
            try:
                num = int(num)
            except ValueError:
                return False
    return True


def check_exit(num_of_list: list) -> bool:
    for num in num_of_list:
        if num == 'X':
            return True
    return False


def sum_of_num(num_of_list: list) -> int:
    sum = 0
    for num in num_of_list:
        if num == 'X':
            break
        else:
            num = int(num)
            sum = num + sum
    return sum


sum = 0
while True:
    str_of_num = input('Введите строку чисел, разделенных пробелами: ')
    list_of_num = str.split(str_of_num)

    if check_list(list_of_num):
        sum = sum_of_num(list_of_num) + sum
    else:
        print("Не верное значение данных\n")
        continue
    if check_exit(list_of_num):
        break
print(f'Сумма чисел равна {sum}')
