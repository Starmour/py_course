students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код

"""
Список пар "ID студента — возраст": [(1, 23), (2, 24), (3, 22)]
Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
Общая длина всех фамилий студентов: 20
"""


def get_id_age_pair(in_dict):
    id_age_list = [(key, in_dict[key]["age"]) for key in in_dict.keys()]
    print("The list of pairs \"ID - Age\":", id_age_list)
    return id_age_list


def get_interests(in_dict):
    interests_list = [in_dict[key]["interests"] for key in in_dict.keys()]
    new_list = []
    for el in interests_list:
        for interest in el:
            new_list.append(interest)

    print("Full list of students' interests:", new_list)


def get_total_surname_len(in_dict):
    surname_len_list = [len(in_dict[key]["surname"]) for key in in_dict.keys()]
    summ = 0
    for el in surname_len_list:
        summ += int(el)
    print("Total length of students' surnames:", summ)


get_id_age_pair(students)
get_interests(students)
get_total_surname_len(students)
