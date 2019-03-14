#!/usr/bin/env python
# coding: utf-8


def check_argument(x):
    return (type(x) is int) or (type(x) is float)


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if check_argument(x) and check_argument(y):
        if operator == "plus":
            return x+y
        if operator == "minus":
            return x-y
        if operator == "divide":
            if y != 0:
                return x/y
            else:
                return None
        if operator == "mult":
            return x*y
    return None
    raise NotImplementedError
