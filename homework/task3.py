'''
3. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''


def chek_unic(el, lister):
    i = 0
    for _ in lister:
        if _ == el:
            i += 1
    if i > 1:
        return False
    else:
        return True


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_set = set(my_list)
print(my_list[1:])
unic_list = [el for el in my_list if chek_unic(el, my_list)]
print(unic_list)
