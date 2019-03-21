#!/usr/bin/env python
# coding: utf-8

import time
import collections


class LRUCacheDecorator:
    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = collections.OrderedDict()
        self.time = time.time()

    def __call__(self, func):
        # TODO вызов функции
        def clearing():
            if self.ttl and time.time() - self.time >= self.ttl:
                self.time = time.time()
                self.cache.clear()

        def out(*args):
            clearing()
            if args in self.cache:
                result = self.cache[args]
                del self.cache[args]
                self.cache[args] = result
                return result
            if self.maxsize:
                if len(self.cache) < self.maxsize:
                    self.cache[args] = func(*args)
                else:
                    self.cache.popitem(last=False)
                    self.cache[args] = func(*args)
            else:
                self.cache[args] = func(*args)
            return self.cache[args]
        return out
