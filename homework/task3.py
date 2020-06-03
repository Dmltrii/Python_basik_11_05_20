'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
'''

line_list = []
with open("To_task3.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line_list.append(line.split())
i = 0
sum = 0

for line in line_list:
    if int(line[1]) > 20000:
        print(line[0])
    sum = int(line[1]) + sum
    i += 1
mid_sum = sum / i
print(f'средняя сумма :{mid_sum}')

