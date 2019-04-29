#!/usr/bin/env python
# coding: utf-8


import numpy as np
from collections import Counter


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(self, max_depth=None, min_leaf_size=None, max_leaf_number=None, min_inform_criter=None):
        '''
        Инициализируем наше дерево
        :param max_depth: один из возможных критерием останова - максимальная глубина дерева
        :param min_leaf_size: один из возможных критериев останова - число элементов в листе
        :param max_leaf_number: один из возможных критериев останова - число листов в дереве.
        Нужно подумать как нам отобрать "лучшие" листы
        :param min_inform_criter: один из критериев останова - процент прироста информации, который
        считаем незначительным
        '''
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.max_leaf_number = max_leaf_number
        self.min_inform_criter = min_inform_criter
        self.depth = 0
        self.leaf_number = 0
        self.tree_list = []
        self.classes = []

    def compute_split_information(self, y, th=None):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        if th is None:
            return sum((i / len(y)) ** 2 for i in Counter(y).values())
        else:
            left = th * self.compute_split_information(y[:th])
            right = (len(y) - th) * self.compute_split_information(y[th:])
            return (left + right) / len(y)

    def conditions(self, y):
        one = (self.max_depth is not None) and (self.depth >= self.max_depth)
        three = (self.min_leaf_size is not None) and (len(y) <= self.min_leaf_size) or (len(y) < 2)
        four = len(y) > 1 and (False not in [y[i] == y[i + 1] for i in range(len(y) - 1)])
        return one or three or four

    def fit(self, X, y, t=None, depth=0):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        if self.depth < depth:
            self.depth = depth
        if len(self.classes) == 0:
            self.classes = Counter(y).keys()
        if self.conditions(y):
            self.leaf_number += 1
            cnt = Counter(y)
            if t is not None:
                t.append({i: cnt[i] / len(y) for i in self.classes})
            else:
                self.tree_list = [{i: cnt[i] / len(y) for i in self.classes}]
            return
        max_info = max_th = max_feature = 0
        for i in range(X.shape[1]):
            xy = np.array(sorted(zip(X[:, i], y), key=lambda k: k[0]))
            x_train, y_train = xy[:, 0], xy[:, 1]
            for j in range(y_train.shape[0] - 1):
                if y_train[j] != y_train[j+1]:
                    new_max_info = self.compute_split_information(y_train, th=j+1)
                    if max_info < new_max_info:
                        max_th = x_train[j]
                        max_info = new_max_info
                        max_feature = i
        if t is None:
            self.tree_list = [max_feature, max_th, [], []]
            self.fit(X[X[:, max_feature] > max_th], y[X[:, max_feature] > max_th], self.tree_list[2],
                     depth + 1)
            self.fit(X[X[:, max_feature] <= max_th], y[X[:, max_feature] <= max_th], self.tree_list[3],
                     depth + 1)
        else:
            t.append(max_feature)
            t.append(max_th)
            t.append([])
            t.append([])
            self.fit(X[X[:, max_feature] > max_th], y[X[:, max_feature] > max_th], t[2], depth + 1)
            self.fit(X[X[:, max_feature] <= max_th], y[X[:, max_feature] <= max_th], t[3], depth + 1)

    def predict(self, X, t=None):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        if self.tree_list is []:
            return ValueError
        if t is None:
            t = self.tree_list
        if type(t[0]) is dict:
            return np.array([max(t[0], key=lambda x:t[0][x])]*X.shape[0])
        else:
            classes = np.zeros((X.shape[0],))
            if X[X[:, t[0]] > t[1]].shape[0] != 0:
                classes[X[:, t[0]] > t[1]] = self.predict(X[X[:, t[0]] > t[1]], t=t[2])
            if X[X[:, t[0]] <= t[1]].shape[0] != 0:
                classes[X[:, t[0]] <= t[1]] = self.predict(X[X[:, t[0]] <= t[1]], t=t[3])
            return classes

    def predict_proba(self, X, t=None):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        if self.tree_list is []:
            return ValueError
        if t is None:
            t = self.tree_list
        if type(t[0]) is dict:
            return np.array([list(t[0].values()) for _ in range(X.shape[0])])
        else:
            probas = np.zeros((X.shape[0], len(self.classes)))
            if X[X[:, t[0]] > t[1]].shape[0] != 0:
                probas[X[:, t[0]] > t[1]] = self.predict_proba(X[X[:, t[0]] > t[1]], t=t[2])
            if X[X[:, t[0]] <= t[1]].shape[0] != 0:
                probas[X[:, t[0]] <= t[1]] = self.predict_proba(X[X[:, t[0]] <= t[1]], t=t[3])
            return probas
