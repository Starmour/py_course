print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15
num = int(input("Please, input the number \n>"))


def sum_nums(n):
    summ = 0
    for el in range(n + 1):
        summ += el
    print(f"Sum of numbers from 1 to {num} is", summ)


sum_nums(num)
