#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nose.tools import raises

from week2 import conditions


@raises(ValueError)
def test_age_string():
    conditions.get_occupation_by_age('five')


@raises(ValueError)
def test_age_unborn():
    conditions.get_occupation_by_age(-1)


@raises(TypeError)
def test_age_none():
    conditions.get_occupation_by_age(None)


@raises(TypeError)
def test_age_list():
    conditions.get_occupation_by_age([])


def test_ages():
    test_cases = [
        (0, 'kindergarten'),
        (0.2, 'kindergarten'),  # float
        ('3', 'kindergarten'),  # string(int)
        (6, 'kindergarten'),
        (7, 'school'),
        (16, 'school'),
        (17, 'university'),
        (20, 'university'),
        (21, 'work'),
        (59, 'work'),
        (60, 'retirement')
    ]
    for age, occupation in test_cases:
        yield check_age, age, occupation


def check_age(age, occupation):
    assert conditions.get_occupation_by_age(age) == occupation


def test_compare_strings():
    test_cases = [
        # first, second, result
        (1, 'two', 0),
        ('one', None, 0),
        ('same', 'same', 1),
        ('', '', 1),
        ('learn', 'learn', 1),
        ('longer string', 'shorter', 2),
        ('', 'learn', 3),
        ('shorter', 'longer string', None),
    ]

    for first, second, result in test_cases:
        yield check_compare_strings, first, second, result


def check_compare_strings(first, second, result):
    strings = conditions.compare_strings(first, second)
    assert strings == result
