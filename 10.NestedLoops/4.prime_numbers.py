print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.
while True:
    num_count = int(input("Please enter count of numbers\n>"))
    prime_num = 0
    for num in range(num_count):
        input_num = int(input("Please enter the number\n>"))
        counter = 0
        for div in range(2, input_num):
            if input_num % div == 0:
                counter += 1
        if counter == 0:
            prime_num += 1

    print("Count of prime numbers is", prime_num)
