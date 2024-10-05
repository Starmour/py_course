print('Задача 5. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку. Ему особенно понравилась книга «Преступление и наказание». Паоло решил найти самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.

# Что нужно сделать

# Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём. Слова в тексте разделяются одним пробелом.

# Пример:

# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.

# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв

# while True:
text = input("Please, enter the text\n>")

# text = "Every hunter wants to know where the pheasant are sitting"
# text = "1234 12345 123612 "
# #                 11111111
# #       123456789012345678
longest_word = ""
new_word = ""

for letter in text:
    new_word += letter
    if letter == " ":
        print(new_word)
        if len(new_word) > len(longest_word):
            longest_word = new_word
        new_word = ""

print(
    f"The longest word in the text is \"{longest_word.upper()}\" with the length of {len(longest_word.strip())} letters"
)
