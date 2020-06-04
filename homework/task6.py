'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import os

schedule_path = os.path.join(os.path.dirname(__file__), 'to_task6')
db_dict = {}
line_list = []
sub_name = []
sub_hours = []
sub_hour = []
with open(schedule_path, 'r', encoding='utf-8') as file:
    for line in file:
        sub_name = []
        sub_hours = []
        sub_hour = []
        sum_h = []
        tmp_dict = {}
        sub_name.append(line.split(':'))
        sub_hours.append(line.split('('))
        for _ in sub_hours:
            for __ in _:
                # print(__)
                sub_hour.append(__.split())
        for _ in sub_hour:
            for __ in _:
                if __.isdigit():
                    sum_h.append(int(__))
        sum_h = sum(sum_h)
        tmp_dict[sub_name[0][0]] = sum_h
        db_dict.update(tmp_dict)
print(db_dict)
