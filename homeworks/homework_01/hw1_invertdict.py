#!/usr/bin/env python
# coding: utf-8


def expand(y, l):
    if (type(y) != tuple) and (type(y) != set) and (type(y) != list):
        l.append(y)
    else:
        for i in y:
            expand(i, l)


def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return None
    else:
        out_dict = {}
        for x, y in source_dict.items():
            l = []
            expand(y, l)
            for i in range(len(l)):
                if l[i] in out_dict.keys():
                    if isinstance(out_dict[l[i]], list):
                        out_dict[l[i]].append(x)
                    else:
                        out_dict[l[i]] = [out_dict[l[i]]]
                        out_dict[l[i]].append(x)

                else:
                    out_dict[l[i]] = x
        return out_dict
    raise NotImplementedError
