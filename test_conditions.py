#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nose.tools import raises

from conditions import conditions


@raises(ValueError)
def test_string():
    conditions.get_occupation_by_age('five')


@raises(ValueError)
def test_unborn():
    conditions.get_occupation_by_age(-1)


def test_ages():
    ages = [0, 0.2, 6,
            7, 16,
            17, 20,
            21, 59,
            60]
    occupations = [
        'kindergarten',
        'kindergarten',
        'kindergarten',
        'school',
        'school',
        'university',
        'university',
        'work',
        'work',
        'retirement'
    ]
    for age, occupation in zip(ages, occupations):
        yield check, age, occupation


def check(age, occupation):
    assert conditions.get_occupation_by_age(age) == occupation
