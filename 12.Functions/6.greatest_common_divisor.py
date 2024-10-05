import math

print('Задача 6. НОД')


def gcd_1(num_1, num_2):
    gr_com_div = 0
    if num_1 < num_2:
        min_num = num_1
    else:
        min_num = num_2
    for el in range(min_num, 0, -1):
        if num_1 % el == 0 and num_2 % el == 0:
            gr_com_div = el
            break
    print("The greatest common divisor is", gr_com_div)


# num_1 = 30
# num_2 = 18
# 36 = 18 * 1 + 12
# 18 = 12 * 1 + 6
# 12 = 6 * 2 + 0
def gcd_2(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    print('The greatest common divisor 1s', num_1 + num_2)

def gcd_3 (num_1, num_2):
    print('The greatest common divisor 1s', math.gcd(num_1,num_2))
while True:
    num_1 = int(input("Please enter the 1st number\n>"))
    num_2 = int(input("Please enter the 2nd number:\n>"))
    gcd_1(num_1, num_2)
    gcd_2(num_1, num_2)
    gcd_3(num_1, num_2)
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел
