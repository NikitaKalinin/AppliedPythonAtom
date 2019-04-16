#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.cof = lambda_coef
        self.type = regulatization
        self.alpha = alpha
        self.weights = None

    def fit(self, X_train, y_train, iterat=1000):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x_new = np.concatenate((np.ones((X_train.shape[0], 1)), (X_train - X_train.mean()) / X_train.std()), axis=1)
        self.weights = np.zeros(x_new.shape[1])
        for _ in range(iterat):
            dl = np.array([np.dot(x_new[:, col], (np.dot(x_new, self.weights) - y_train))
                           for col in range(x_new.shape[1])]) / x_new.shape[0]
            if self.type is None:
                self.weights -= self.cof * dl
            else:
                if self.type == 'L1':
                    self.weights -= self.cof * (dl + self.alpha*np.sign(self.weights))
                elif self.type == 'L2':
                    self.weights -= self.cof * (dl + self.alpha*self.weights)
                else:
                    raise ValueError

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.weights is not None:
            x_new = np.concatenate((np.ones((X_test.shape[0], 1)), (X_test - X_test.mean()) / X_test.std()), axis=1)
            return np.dot(x_new, self.weights)
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
