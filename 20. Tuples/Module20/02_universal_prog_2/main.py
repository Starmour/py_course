# TODO здесь писать код
"""
Пример вызова функции:
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
Ответ в консоли: [2, 3, 5, 7]
"""
import math
from re import match


def crypto(in_set):
    return [is_prime(el) for el in in_set]


def is_prime(num):
    if num in range(0,3):
        return num
    for el in range(2, num):
        if num % el == 0:
            return False

        else:
            return num


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
