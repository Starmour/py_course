print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
while True:
    num = int(input("Please, enter the number:\n>"))
    sym = num
    for row in range(num):
        for left_part in range(num, num - row - 1, -1):
            print(f"{left_part}", end=" ")
        for points in range((num - row) * 2 - 2):
            print(".", end=" ")
        for right_part in range(num - row, num + 1):
            print(f"{right_part}", end=" ")

        print(" ")
