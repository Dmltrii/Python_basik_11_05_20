# Task6

km_first_day = input('Введите количество километров, которые спортсмен пробегает за первый день: ')
while not (int(km_first_day.isdigit())):
    print('Не коректный ввод')
    km_first_dayenue = input('Введите количество километров, которые спортсмен пробегает за первый день: ')
km_first_day_float = float(km_first_day)

km_waiting_this_day = input('Введите количество километров, которые спортсмен должен пробежать: ')
while not (int(km_waiting_this_day.isdigit())):
    print('Не коректный ввод')
    km_waiting_this_day = input('Введите количество километров, которые спортсмен должен пробежать: ')
km_waiting_this_day_float = float(km_waiting_this_day)

day_counter = 1
while km_first_day_float <= km_waiting_this_day_float:
    km_first_day_float = km_first_day_float * 0.1 + km_first_day_float
    day_counter += 1
#   print(day_counter, km_first_day_float)
print(f'На {day_counter}-й день спортсмен достиг результата — не менее {km_waiting_this_day_float} км')
