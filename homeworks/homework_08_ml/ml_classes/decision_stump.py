#!/usr/bin/env python
# coding: utf-8


import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.y1 = self.y2 = self.th = 0

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        xy = np.array(sorted(zip(X, y), key=lambda k: k[0])).T
        x_train, y_train = xy[0], xy[1]
        idx = np.argmin([(np.var(y_train[:i]) * i + np.var(y_train[i:]) * (y_train.shape[0] - i)) / y_train.shape[0]
                        for i in range(2, y_train.shape[0] - 2)])
        self.th, self.y1, self.y2 = x_train[idx], np.mean(y_train[:idx]), np.mean(y_train[idx:])

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        return [self.y2 if x > self.th else self.y1 for x in X]
