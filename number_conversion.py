from string import digits
from string import ascii_uppercase
"""
импортируем из модуля strings: 
string.digits --> The string '0123456789'.
string.ascii_uppercase --> The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 
This value is not locale-dependent and will not change.
"""


mod_str = digits + ascii_uppercase    # СОЗДАЕМ ПЕРЕМЕННУЮ ДЛЯ УДОБСТВА ИСПОЛЬЗОВАНИЯ (КОНСТАНТ МОДУЛЯ)


def converter(number, sys_calculus):
    res_str = []
    while number:
        res_str.insert(0, mod_str[number % sys_calculus])  # ДОБАВЛЯЕМ ОСТАТКИ В НАЧАЛО СПИСКА
        number //= sys_calculus                            # ЧИСЛО ДЕЛИМ НА С.ИСЧИСЛЕНИЯ

    res_str = ''.join(res_str)                             # СКЛЕИВАЕМ ПЕРЕВЕРНУТЫЙ СПИСОК СНАЧЕНИЙ
    return res_str


us_num = int(input('Пожалуйста, введите число: '))
us_system = int(input('Пожалуйста, введите систему исчисления: '))

conversion_result = converter(us_num, us_system)
print('Результат конвертации:', conversion_result)
