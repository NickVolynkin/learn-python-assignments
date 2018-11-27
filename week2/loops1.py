#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import random
import statistics


def loops1():
    print(range(2, 12))


def loops2():
    input_string = input('string to print')
    print(one_char_by_line(input_string))


def one_char_by_line(input_string):
    return '\n'.join(input_string.split())


def generate_random_grades(number):
    """
    Generate a random student with a class label and a list of grades
    :param number:
    :return:
    """

    def rnd_class_label():
        return str(random.randint(1, 11)) + \
               random.choice(['а', 'б', 'в', 'г', 'д'])

    def rnd_grades():
        """
        3 to 7 marks, each varies from 2 to 5.
        :return:
        """
        return [random.randint(2, 5) for _ in range(random.randint(3, 7))]

    for i in range(number):
        yield {
            'school_class': rnd_class_label(),
            'scores': rnd_grades()
        }


def get_avg_school_grade(students):
    """
    Get grade point average for all students
    :param students: [{'school_class': 'str', scores: [int]}, ...]
    :return:
    """
    chain = itertools.chain.from_iterable([student['scores'] for student in students])
    return statistics.mean(chain)


def get_avg_class_grade(students, class_label):
    """
    Get grade point average for a given class
    :param students: [{'school_class': 'str', scores: [int]}, ...]
    :param class_label:
    :return:
    """
    class_marks = filter(lambda student: student['school_class'] == class_label, students)
    chain = itertools.chain.from_iterable([student['scores'] for student in class_marks])
    return statistics.mean(chain)


def list_class_labels(students):
    """
    Get a list of unique class labels, sorted 1st to 11th
    :param students:
    :return:
    """

    classes_set = set([student['school_class'] for student in students])
    classes_list = sorted(list(classes_set), key='{:0>3}'.format)
    return classes_list


def main():
    students = list(generate_random_grades(1000))
    print('{} students'.format(len(students)))
    avg_school = get_avg_school_grade(students)
    print('average school mark: {:.3f}'.format(avg_school))
    print('average class marks:')

    for class_label in list_class_labels(students):
        print('\t{}: {:.3f}'.format(class_label, get_avg_class_grade(students, class_label)))


if __name__ == '__main__':
    main()
