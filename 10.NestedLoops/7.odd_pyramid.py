print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#   0  1 2  3  4  5   6  7  8
# 0             1
# 1          3     5
# 2       7     9     11
# 3    13    15    17    19
# 4 21    23    25    27    29

while True:
    num = int(input("Please, enter the number:\n>"))
    counter = -1
    for row in range(num):
        print((num - row - 1) * "   ", end="")
        for col in range(row + 1):
            counter += 2
            print(counter, end="    ")
        print("")
