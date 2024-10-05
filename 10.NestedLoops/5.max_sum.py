print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
while True:
    num_count = int(input("Please enter count of numbers\n>"))
    max_sum = 0
    num_max_sum = 0
    for num in range(num_count):
        sign_sum = 0
        number = input("Please enter the number\n>")
        # Ввод чисел в соответсии с введенным количеством
        for sign in number:
            # Для каждого знака числа
            num_sign = int(sign)
            # Форматировать его в число
            sign_sum += num_sign
            # Прибавить к переменной суммы знаков
            if sign_sum >= max_sum:
                max_sum = sign_sum
                num_max_sum = number
    print(f"MAX SUM ({max_sum}) OF DIGITALS HAVE NUMBER {num_max_sum}")
