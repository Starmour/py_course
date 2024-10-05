import random
from random import choice

print('Задача 7. Недоделка')


# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    figures = ["Rock", "Paper", "Scissors"]
    rang_fig = choice(figures)
    user_fig = input("Please choose the figure\n#1. Rock\n#2. Paper\n#3. Scissors\n>")
    if user_fig == "1":
        user_fig = "Rock"
    elif user_fig == "2":
        user_fig = "Paper"
    elif user_fig == "3":
        user_fig = "Scissors"
    print(user_fig)


def guess_the_number():
    # Здесь будет игра "Угадай число"
    rand_num = random.randint(1, 10)
    while True:
        user_num = int(input("Please enter the number from 1 to 10\n>"))
        if user_num == rand_num:
            print("CONGRATUlATION! YOU ARE WON !!!")
            break
        else:
            print("Please, try again")


def main_menu():
    while True:
        invite = input("Please choose the game\n#1. Rock Paper Scissor\n#2. Guess the number\n>")
        if invite == "1":
            rock_paper_scissors()
        if invite == "2":
            guess_the_number()


main_menu()

# Здесь главное меню игры
