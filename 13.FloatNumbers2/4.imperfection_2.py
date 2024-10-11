import math

print('Задача 4. Недоделка 2')


# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код согласно следующим условиям: программа получает на вход два числа;
# в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом
# и как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код,
# чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя,
# выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def count_numbers(num, num_size):
    if len(num) >= num_size:
        return int(num)
    else:
        print(f"The length of number must be as least {num_size} digits")


def change_number(num):
    count = 0
    first_dig = ""
    last_dig = ""
    mid_digs = ""
    num = str(num)
    for el in num:
        count += 1
        if count == 1:
            first_dig = el
        elif count == len(num):
            last_dig = el
        else:
            mid_digs += el
    # print(f"The first digit of {num} is {first_dig}")
    # print(f"The last digit of {num} is {last_dig}")
    # print(f"The middle digits of {num} is {mid_digs}")
    num = last_dig + mid_digs + first_dig
    print(f"The changed number is:", num)


def main():
    first_num = input("Please, enter the first number: \n>")
    second_num = input("Please, enter the second number: \n>")

    num_1 = count_numbers(first_num, 3)
    num_2 = count_numbers(second_num, 4)
    change_number(num_1)
    change_number(num_2)


while True:
    main()
