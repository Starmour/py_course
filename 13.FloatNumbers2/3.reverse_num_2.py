print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse(num):
    rev_num = int(str(num)[::-1])
    return rev_num


while True:
    num_1 = input("Please enter the 1st number:\n>")
    num_2 = input("Please enter the 2nd number:\n>")

    rev_num_1 = reverse(num_1)
    rev_num_2 = reverse(num_2)
    sum = rev_num_1 + rev_num_2
    rev_sum = reverse(sum)
    print(f"The 1st reversed number {num_1} is", rev_num_1)
    print(f"The 2nd reversed number {num_2} is", rev_num_2)
    print("The summ of reversed numbers is", sum)
    print("The reversed summ of reversed numbers is", rev_sum)
