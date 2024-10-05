print('Задача 6. НОД')
while True:
    num_1 = int(input("Please enter the 1st number\n>"))
    num_2 = int(input("Please enter the 2nd number:\n>"))
    gr_com_div = 0
    if num_1 < num_2:
        min_num = num_1
    else:
        min_num = num_2
    for el in range(min_num, 0, -1):
        if num_1 % el == 0 and num_2 % el == 0:
            gr_com_div = el
            break
    print("The great common divisor is", gr_com_div)


#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
