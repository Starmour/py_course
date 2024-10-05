print('Задача 3. Театр\n \n !!! НЕТ ПРОБЕЛОВ !!!\n')
# В городе планируют построить театр под открытым небом, но для начала нужно оценить, сколько сделать рядов, сидений в них и каким должно быть расстояние между рядами.

# Что нужно сделать

# Напишите программу, которая получает на вход количество рядов, сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран.


# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
rows_count = int(input("Please input rows count:\n>"))
seats_count = int(input("Please input seats count:\n>"))
gap_length = int(input("Please input gap length:\n>"))

for row in range(rows_count):
    seat_sign = ""
    for seat in range(seats_count):
        seat_sign += "*"
    for gap in range(gap_length):
        seat_sign += "="
    for seat in range(seats_count):
        seat_sign += "*"
    print(seat_sign)
