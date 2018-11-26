#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_occupation_by_age(age):
    # will raise TypeError or ValueError if not a number
    age = int(age)

    if age < 0:
        raise ValueError("person cannot have age less than zero")
    elif age < 7:
        return "kindergarten"
    elif age < 17:
        return "school"
    elif age < 21:
        return "university"
    elif age < 60:
        return "work"
    else:
        return "retirement"


def compare_strings(first, second):
    if not type(first) == type(second) == str:
        return 0
    elif first == second:
        return 1
    elif len(first) > len(second):
        return 2
    elif second == 'learn':
        return 3
    else:
        return None

