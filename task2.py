# Task2

time_in_sec = input('Введите количество секунд: ')

# check number
while not (int(time_in_sec.isdigit())):
    print('Не коректный ввод')
    time_in_sec = input('Введите количество секунд:')

time_in_sec_int = int(time_in_sec)

hours_num = time_in_sec_int // 360
if (hours_num < 10):
    hours_str = '0' + str(hours_num)
else:
    hours_str = str(hours_num)

min_num = (time_in_sec_int % 360) // 60

if (min_num < 10):
    min_str = '0' + str(min_num)
else:
    min_str = str(min_num)

sec_num = time_in_sec_int % 60

if (sec_num < 10):
    sec_str = '0' + str(sec_num)
else:
    sec_str = str(sec_num)

print(f"Время: {hours_str}:{min_str}:{sec_str}")
