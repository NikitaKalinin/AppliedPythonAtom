#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return ((y_true - y_hat)**2).mean()


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return (abs(y_true - y_hat)).mean()


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    z = sum((y_true - y_true.mean()) ** 2)
    if z == 0:
        return 0
    else:
        return 1 - sum((y_true - y_hat)**2) / z
