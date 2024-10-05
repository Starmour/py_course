import math

print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

while True:
    print("Please, enter the position of horse:")
    x_pos = float(input("> x:"))
    y_pos = float(input("> y:"))

    # + В условии if x_pos > 8 or y_pos > 8: учитывается только верхняя граница доски, но отсутствует проверка на нижнюю границу (координаты должны быть в диапазоне от 0 до 8). Например, координата -0.5 не будет проверена как недопустимая.
    # if x_pos > 8 or y_pos > 8:
    if x_pos > 8 or y_pos > 8 or x_pos < 0 or y_pos < 0:
        print("The horse can not start from this point(\nPlease enter correct coordinations!\n")
    else:
        print("\nPlease, enter the destination point:")
        x_point = float(input("> x:"))
        y_point = float(input("> y:"))
        # + Использование math.ceil не совсем корректно для определения клетки на доске. Например, если координата x_pos = 0.5, то результат math.ceil(x_pos) будет 1, что смещает клетку на одну единицу вверх. Лучше округлять до ближайшего целого числа, используя round()
        print(
            f"The horse stay at {round(x_pos)},{round(y_pos)} square.\nDestination point is on {round(x_point)},{round(y_point)} square\n")

        # + В условии if (x_point <= 8 or y_point <= 8) тоже недостаёт проверки на нижнюю границу.
        # ? Условие if (abs(x_pos - x_point) == 1 and abs(y_pos - y_point) == 2) or (abs(x_pos - x_point) == 2 and abs(y_pos - y_point) == 1): проверяет корректность хода коня, но оно должно быть связано с проверкой допустимости координат.
        # + Условие в строке if (x_point <= 8 or y_point <= 8) должно быть с логическим оператором "и" (and), так как нужно убедиться, что обе координаты точки находятся в пределах доски.

        if (x_point <= 8 and y_point <= 8) and (x_point >= 0 and y_point >= 0) and (
                (abs(x_pos - x_point) == 1 and abs(y_pos - y_point) == 2) or (
                abs(x_pos - x_point) == 2 and abs(y_pos - y_point) == 1)):
            print("The horse MAY stay at this point! \n")
        else:
            print("The horse can NOT stay on this point(\nPlease enter correct coordinations!\n")
