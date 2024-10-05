print('Задача 3. Апгрейд калькулятора')


# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются
# не только обычные арифметические действия.

# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом:
# вывести сумму его цифр, максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def operation(num, oper):
    if oper == "1":
        add(num)
    elif oper == "2":
        multiplicate(num)
    elif oper == "3":
        maximum(num)
    elif oper == "4":
        minimum(num)
    else:
        print("INVALID INPUT! PLEASE, ENTER CORRECT DATA")


def add(num):
    result = 0
    for el in num:
        el = int(el)
        result += el
    print("The result of addition is", result)


def multiplicate(num):
    result = 1
    for el in num:
        el = int(el)
        result *= el
    print("The result of multiplication is", result)


def maximum(num):
    max_num = 0
    for el in num:
        el = int(el)
        if el >= max_num:
            max_num = el
    print("The max digital is", max_num)


def minimum(num):
    min_num = int(num)
    for el in num:
        el = int(el)
        if el < min_num:
            min_num = el
    print("The min digital is", min_num)


while True:
    enter = input("Please, enter the number:\n>")
    oper = input(
        "Please, choose the operation:\n1) ADDITION;\n2) MULTIPLICATION;\n3) FIND MAX DIGITAL;\n4) FIND MIN DIGITAL.\n>")

    operation(enter, oper)
