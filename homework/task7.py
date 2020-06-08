'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
import os

firm_path = os.path.join(os.path.dirname(__file__), 'to_task7')
db_dict = {}
average_profit = 0

with open(firm_path, 'r', encoding='utf-8') as file:
    for line in file:
        data = [line.split(' ')]
        profit = int(data[0][2]) - int(data[0][3])
        db_dict[data[0][0]] = profit
        if profit > 0:
            average_profit = average_profit + profit
average_profit_dict = {"average_profit": average_profit}
db_list = [db_dict, average_profit_dict]
print(db_list)
with open("my_file.json", "w") as write_f:
    json.dump(db_list, write_f)
