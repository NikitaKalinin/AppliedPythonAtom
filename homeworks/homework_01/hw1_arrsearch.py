#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    a = input_list
    for i in range(len(a)):
        if (n-a[i]) in a:
            if a[i] != n-a[i]:
                out = (i, a.index(n-a[i]))
                return out
    return None
    raise NotImplementedError
