#!/usr/bin/env python
# coding: utf-8

import itertools
from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return True if key in self else default_value

    def put(self, key):
        # TODO метод put, нужно переопределить данный метод
        if key not in self:
            super().put(key, None)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.capacity

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        out = HashSet()
        for key in itertools.chain(self.keys(),another_hashset.keys()):
            if key in self.keys() and key in another_hashset.keys():
                out.put(key)
        return out
