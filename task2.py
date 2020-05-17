"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
использовать функцию input().
"""

var_str = input('Введите элементы списка разделенные пробелами: ')
var_list = var_str.split()

lenth = len(var_list)
tmp_list = []
i = 0
while i < (lenth - 1):
    tmp_list.append(var_list[i+1])
    tmp_list.append(var_list[i])
    i += 2
if len(var_list) % 2 != 0:
    tmp_list.append(var_list[lenth - 1])
print(tmp_list)
