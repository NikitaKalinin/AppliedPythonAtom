#!/usr/bin/env python
# coding: utf-8


import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    a = a.astype(float, copy=False)
    b = b.astype(float, copy=False)
    c = -c.astype(float, copy=False)
    c = np.append(c, [0]*len(b))
    horiz_x = [i for i in range(len(c))]
    vert_x = [i+a.shape[1] for i in range(len(b))]
    out = np.zeros(a.shape[1])
    a = np.concatenate((a, np.eye(len(b), dtype=float)), axis=1)
    # если в разрешающем столбце есть нули делю на 0, получится inf., он явно не минимум
    simpl = lambda x: x if x >= 0 else 0
    while True in (c < 0):
        piv_col = np.argmin(c)
        if True in (a[:, piv_col] > 0):
            piv_row = np.argmin(np.array([b[i] / simpl(a[i, piv_col]) for i in range(len(b))]))
            horiz_x[piv_col], vert_x[piv_row] = vert_x[piv_row], horiz_x[piv_col]
            b[piv_row] = b[piv_row] / a[piv_row, piv_col]
            a[piv_row] = a[piv_row] / a[piv_row, piv_col]
            c = c - c[piv_col]*a[piv_row]
            for i in range(len(a)):
                if i != piv_row:
                    b[i] = b[i] - a[i, piv_col]*b[piv_row]
                    a[i] = a[i] - a[i, piv_col]*a[piv_row]
        else:
            c[piv_col] = 0
    for i in range(len(b)):
        print(i)
        if vert_x[i] < len(out):
            out[vert_x[i]] = b[i]
    return out
