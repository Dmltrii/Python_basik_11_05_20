# Task5

revenue = input('Введите значение выручки фирмы: ')
while not (int(revenue.isdigit())):
    print('Не коректный ввод')
    revenue = input('Введите значение выручки фирмы: ')
revenue_int = int(revenue)

cost = input('Введите значение издержек фирмы: ')
while not (int(cost.isdigit())):
    print('Не коректный ввод')
    cost = input('Введите значение издержек фирмы: ')
cost_int = int(cost)

if revenue_int > cost_int:
    print('Фирма получает прибыль.')
    profitability = revenue_int / cost_int
    print(f'Рентабельность выручки {profitability}')
    number_of_persons = input('Введите численность сотрудников фирмы: ')
    while not (int(number_of_persons.isdigit())):
        print('Не коректный ввод')
        number_of_persons = input('Введите численность сотрудников фирмы: ')
    number_of_persons_int = int(number_of_persons)
    profitability_to_person = revenue_int / number_of_persons_int
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {profitability_to_person}')
elif revenue_int == cost_int:
    print('Фирма ничего не заробатывает.')
else:
    print('Фирма работает в убыток.')
