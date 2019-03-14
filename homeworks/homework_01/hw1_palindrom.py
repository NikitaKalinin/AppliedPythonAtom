#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    l = len(input_string)
    if 0 <= l <= 1:
        return True
    else:
        if input_string[0] == input_string[l-1]:
            return check_palindrom(input_string[1:l-1])
        else:
            return False
    raise NotImplementedError
