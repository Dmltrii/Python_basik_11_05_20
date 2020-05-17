product_list = []
enter = True
i = 0
while enter:
    product_list.append(i)
    product_name = input('Введите название товара: ')
    while True:
        product_cost = input('Введите цену товара: ')
        if product_cost.isdigit():
            product_cost = int(product_cost)
            break
        else:
            print('Ошибка ввода')
    while True:
        product_quantity = input('Введите количество товара: ')
        if product_quantity.isdigit():
            product_quantity = int(product_quantity)
            break
        else:
            print('Ошибка ввода')
    product_unit = input('Введите еденицу измерения товара: ')

    product_dict = {'название': product_name, 'цена': product_name, 'количество': product_quantity, 'ед.': product_unit}
    tmp_product_list = (i + 1, product_dict)
    product_tuple = tuple(tmp_product_list)

    product_list[i] = product_tuple

    check_exit = input(
        '\nЧтобы закончить ввод наберите exit и нажмите клавищу "Enter",\nчтобы продолжить нажмите клавищу "Enter": ')
    if check_exit == 'exit':
        enter = False
    i += 1

# analysis

tmp_dict = {}
product_name = []
product_cost = []
product_quantity = []
product_unit = []

for number_of_prodact in product_list:
    tmp_dict = number_of_prodact[1]
    product_name.append(tmp_dict.get('название'))
    product_cost.append(tmp_dict.get('цена'))
    product_quantity.append(tmp_dict.get('количество'))
    product_unit.append(tmp_dict.get('ед.'))

analysis_dict = {'название': product_name, 'цена': product_cost, 'количество': product_quantity, 'ед.': product_unit}
print(analysis_dict)
