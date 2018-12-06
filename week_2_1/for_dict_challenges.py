def count_names(persons: list) -> dict:
    """

    :param persons: list of {'first_name': str}
    :return:
    """
    names_counted = {}
    for person in persons:
        person_name = person['first_name']
        if person_name in names_counted:
            names_counted[person_name] += 1
        else:
            names_counted.update({person_name: 1})

    return names_counted


def get_most_common(items_counted: dict) -> tuple:
    """
    :param items_counted: dict: {item_name(str): count(int)}
    :return: tuple: (most common item_name, count)
    """
    items_list = list(items_counted.items())
    # sort list by second item in tuples, which is the name count
    return sorted(items_list, key=lambda x: x[1])[-1]


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_1 = count_names(students)

for name, number in names_1.items():
    print('{}: {}'.format(name, number))
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names_2 = count_names(students)

# list of tuples (key, value) from dict
most_common_name, _ = get_most_common(names_2)
print("Самое частое имя среди учеников: {}".format(most_common_name))
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [
        # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [
        # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
# ???
for number, class_name in enumerate(school_students, start=1):
    clazz_most_common_name, _ = get_most_common(count_names(class_name))
    print('Самое частое имя в классе {}: {}'.format(number, clazz_most_common_name))


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

def count_genders_by_name(persons: list, is_name_male: dict) -> tuple:
    """
    :param persons: list of {'first_name': str}
    :param is_name_male: dict: {str: True for male, False for female}
    :return: tuple(males, females)
    """

    males = sum([1 for person in persons if is_name_male[person['first_name']]])
    return males, len(persons) - males


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4x', 'students': [{'first_name': 'Маша'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def genders_by_class(school):
    for clazz in school:
        males, females = count_genders_by_name(persons=clazz['students'], is_name_male=is_male)
        yield (clazz['class'], males, females )


for class_name, male_students, female_students in genders_by_class(school):
    print('В классе {} {} девочки и {} мальчика.'.format(
        class_name,
        female_students,
        male_students
    ))

# Пример вывода:-
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

classes = list(genders_by_class(school))
# -x[n] to sort list DEC by elemen number n
# [0][0], take top class, take its name
max_males_class = sorted(classes, key=lambda x: -x[1])[0][0]
max_females_class = sorted(classes, key=lambda x: -x[2])[0][0]
print('Больше всего мальчиков в классе {}'.format(max_males_class))
print('Больше всего девочек в классе {}'.format(max_females_class))
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
