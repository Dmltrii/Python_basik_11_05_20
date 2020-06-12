'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:

    def __init__(self, data_str: str):
        self.__data_str = data_str

    @classmethod
    def take_data_num(cls, data_str: str):
        lister = [data_str.split('-')]
        day = int(lister[0][0])
        month = int(lister[0][1])
        year = int(lister[0][2])
        return {'day': day, 'month': month, 'year': year}

    @staticmethod
    def validator(dicter: dict):
        if dicter.get('day') > 31 or dicter.get('day') == 0:
            print('Неверно введен день')
        elif dicter.get('month') > 12 or dicter.get('month') == 0:
            print('Неверно введен день')
        else:
            print('Все хорошо')


print(Data.take_data_num('12-06-1234'))
Data.validator(Data.take_data_num('12-06-1234'))
print(Data.take_data_num('44-06-1234'))
Data.validator(Data.take_data_num('44-06-1234'))