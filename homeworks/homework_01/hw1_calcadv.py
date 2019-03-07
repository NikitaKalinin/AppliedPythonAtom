#!/usr/bin/env python
# coding: utf-8


def check_opr(x):
    if x is "+" or x is "-" or x is "*" or x is "/" or x is "(" or x is ")":
        return True
    else:
        return False


def check_num(x):
    try:
        k = int(x)
        return True
    except:
        return False


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    l = input_string
    l = l.replace(" ", "")
    k = 1
    out_l, opr_l = [], []
    if l is None:
        return None
    for i in range(len(l)):
        k *= int(check_opr(l[i]) or check_num(l[i]))
    if not bool(k):
        return None
    while "--" in l or "++" in l or "+-" in l or "-+" in l:
        l = l.replace("--", "+")
        l = l.replace("++", "+")
        l = l.replace("+-", "-")
        l = l.replace("-+", "-")
    if "**" in l or "//" in l or "*/" in l or "/*" in l:
        return None
    if "*-" in l or "-*" in l or "*+" in l or "+*" in l:
        return None
    if "/-" in l or "-/" in l or "/+" in l or "+/" in l:
        return None
    while l != "":
        s = ""
        while  l != "" and check_num(l[0]):
            s = s + l[0]
            if len(l) > 1:
                l = l[1:]
            else:
                l = ""
        if s != "":
            out_l.append(int(s))
        s = ""
    '''
    raise NotImplementedError
