#!/usr/bin/env python
# coding: utf-8


import itertools


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self.key

        def get_value(self):
            # TODO возвращаем значение
            return self.value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.key == other.get_key()

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.buckets = [[] for i in range(bucket_num)]
        self.capacity = 0

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        if key in self:
            index = self._get_index(self._get_hash(key))
            for entry in self.buckets[index]:
                if entry.key == key:
                    return entry.value
        else:
            return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        try:
            h = hash(key)
        except TypeError:
            return
        index = self._get_index(hash(key))
        if key in self:
            for entry in self.buckets[index]:
                if entry.key == key:
                    entry.value = value
        else:
            self.buckets[index].append(self.Entry(key, value))
            self.capacity += 1
            if (self.capacity/len(self.buckets)) > (2/3):
                self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.capacity

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.buckets)

    def values(self):
        # TODO Должен возвращать итератор значений
        it = 0
        for entries in self.buckets:
            if it == 0:
                it = iter([entry.value for entry in entries])
            else:
                it = itertools.chain(it, iter([entry.value for entry in entries]))
        return it

    def keys(self):
        # TODO Должен возвращать итератор ключей
        it = 0
        for entries in self.buckets:
            if it == 0:
                it = iter([entry.key for entry in entries])
            else:
                it = itertools.chain(it, iter([entry.key for entry in entries]))
        return it

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return zip(self.keys(), self.values())

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        new_buckets = [[] for i in range(len(self.buckets) * 2)]
        for entries in self.buckets:
            for entry in entries:
                index = hash(entry.key) % len(new_buckets)
                new_buckets[index].append(entry)
        self.buckets = new_buckets

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        buckets = ",".join(str(i) for i in self.buckets)
        items = ", ".join(str(i) for i in self.items())
        return 'buckets: {' + buckets + '}, items: {' + items + '}'

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        for bucket in self.buckets:
            for entry in bucket:
                if entry.key == item:
                    return True
        return False
