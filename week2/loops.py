#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import statistics
import itertools


def loops1():
    print(range(2, 12))


def loops2():
    input_string = input('string to print')
    print(one_char_by_line(input_string))


def one_char_by_line(input_string):
    return '\n'.join(input_string.split())


def generate_random_marks(number):
    def rnd_class():
        return str(random.randint(1, 11)) + \
               random.choice(['а', 'б', 'в', 'г', 'д'])

    def rnd_marks():
        """
        3 to 7 marks, each varies from 2 to 5.
        :return:
        """
        return [random.randint(2, 5) for _ in range(random.randint(3, 7))]

    for i in range(number):
        yield {
            'school_class': rnd_class(),
            'scores': rnd_marks()
        }


def get_avg_school_mark(students):
    """
    get average school mark
    :param marks: [{'school_class': '', scores}]
    :return:
    """
    chain = itertools.chain.from_iterable([student['scores'] for student in students])
    return statistics.mean(chain)


def get_avg_class_mark(students, class_name):
    class_marks = filter(lambda student: student['school_class'] == class_name, students)
    chain = itertools.chain.from_iterable([student['scores'] for student in class_marks])
    return statistics.mean(chain)


def get_all_classes(students):
    def sorter(name):
        return int(name[:-1])

    classes_set = set([student['school_class'] for student in students])
    classes_list = sorted(list(classes_set), key=sorter)
    return classes_list


def main():
    students = list(generate_random_marks(1000))
    print('{} students'.format(len(students)))
    avg_school = get_avg_school_mark(students)
    print('average school mark: {}'.format(avg_school))
    print('average class marks:')

    for class_ in get_all_classes(students):
        print('\t{}: {}'.format(class_, get_avg_class_mark(students, class_)))

if __name__ == '__main__':
    main()
