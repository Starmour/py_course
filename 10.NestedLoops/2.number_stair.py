print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input("Please, enter the number:\n>"))

for row in range(num):
    for col in range(num):
        if row >= col:
            print(row + 1, end=" ")
        else:
            print("", end="")
    print("")
