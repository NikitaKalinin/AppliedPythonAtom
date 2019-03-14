#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    i = 0
    a = input_string
    if a is "":
        return True
    else:
        if a[0] is "}" or a[0] is ")" or a[0] is "]":
            return False
        else:
            while i < len(a) and (a[i] is "{" or a[i] is "(" or a[i] is "["):
                i = i + 1
            if i != len(a):
                s = a[i-1] + a[i]
                if s == "[]" or s == "{}" or s == "()":
                    if i == (len(a)-1):
                        new_string = a[:i-1]
                    else:
                        new_string = a[:i-1] + a[i+1:]
                    return is_bracket_correct(new_string)
                else:
                    return False
            else:
                return False
    raise NotImplementedError
