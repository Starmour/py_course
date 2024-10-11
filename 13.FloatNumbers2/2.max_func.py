print('Задача 2. Функция максимума')


# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать.
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
# Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.

def maximum_of_two(num_1, num_2):
    if num_1 > num_2:
        return num_1

    elif num_2 > num_1:
        return num_2
    else:
        return num_1


def maximum_of_three(num_1, num_2, num_3):
    max_1 = maximum_of_two(num_1, num_2)
    max_2 = maximum_of_two(max_1, num_3)
    return max_2

while True:
    num_1 = float(input("Please enter the 1st number:\n>"))
    num_2 = float(input("Please enter the 2nd number:\n>"))
    num_3 = float(input("Please enter the 3rd number:\n>"))
    print(f"The maximum between {num_1} and {num_2} is", maximum_of_two(num_1, num_2))
    print(f"The maximum among {num_1}, {num_2} and {num_3} is",maximum_of_three(num_1, num_2, num_3))



