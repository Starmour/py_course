print('Задача 2. Функция в функции')


# Евгений проходит специальный тест по программированию.
# У него всё шло хорошо, пока он не наткнулся на тему “Функции”.
# 
# Задание звучит так:
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# 
# Это вызов функции test().
# В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова "Положительное".
# 
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".
# 
# Помогите Евгению и реализуйте такую программ


def test(num):
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        zero()


def positive():
    print("Positive")
    test(int(input("Please, enter the number:\n>")))


def negative():
    print("Negative")
    test(int(input("Please, enter the number:\n>")))


def zero():
    print("It is ZER0!")
    test(int(input("Please, enter the number:\n>")))


test(int(input("Please, enter the number:\n>")))
