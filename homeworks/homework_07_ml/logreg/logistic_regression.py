#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.preprocessing import LabelBinarizer, StandardScaler
import math


class LogisticRegression:

    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5, n_iter=1000):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.cof = lambda_coef
        self.type = regulatization
        self.alpha = alpha
        self.weights = None
        self.labels = None
        self.iterat = n_iter
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        lb = LabelBinarizer()
        train_y = lb.fit(y_train).transform(y_train)
        if train_y.shape[1] == 1:
            train_y = np.append(1-train_y, train_y, axis=1)
        self.labels = lb.classes_
        self.weights = np.zeros((train_y.shape[1], X_train.shape[1] + 1))
        self.scaler.fit(X_train)
        train_x = self.scaler.transform(X_train)
        train_x = np.hstack((np.ones((train_x.shape[0], 1)), train_x))
        for _ in range(self.iterat):
            for i in range(train_y.shape[0]):
                deriative = np.zeros((train_y.shape[1], X_train.shape[1] + 1))
                for j in range(train_y.shape[1]):
                    a = -np.dot(train_x[i], self.weights[j])
                    try:
                        deriative[j] += train_x[i] * (1 / (1 + math.exp(a)) - train_y[i, j])
                    except OverflowError:
                        deriative[j] -= train_x[i] * train_y[i, j]
                    if self.type is not None:
                        if self.type == 'L1':
                            deriative[j] += self.alpha * np.sign(self.weights[j])
                        elif self.type == 'L2':
                            deriative[j] += self.alpha * self.weights[j]
                        else:
                            raise ValueError
                self.weights -= self.cof * deriative

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.weights is not None:
            return [self.labels[i] for i in np.argmax(self.predict_proba(X_test), axis=1)]
        else:
            raise ValueError

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        if self.weights is not None:
            out, into = [], []
            test_X = self.scaler.transform(X_test)
            test_X = np.hstack((np.ones((test_X.shape[0], 1)), test_X))
            for row in test_X:
                into = []
                for wths in self.weights:
                    try:
                        a = math.exp(-np.dot(row, wths))
                        into.append(1 / (1 + a))
                    except OverflowError:
                        into.append(0)
                if np.sum(into) != 0:
                    into = into / np.sum(into)
                out.append(list(into))
            return np.array(out)
        else:
            raise ValueError

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self.weights is not None:
            return self.weights
        else:
            raise ValueError
