#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    number = str(number)
    number = number[::-1]
    flag = False
    if number[len(number)-1] == "-":
        number = number[len(number)-1] + number[0:len(number)-1]
        flag = True
    if flag:
        while number[1] == 0 and len(number) >= 2:
            number = number[0] + number[2:]
    else:
        while number[0] == 0 and len(number) >= 1:
            number = number[1:]
    return int(number)
    raise NotImplementedError
