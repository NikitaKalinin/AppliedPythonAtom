#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.preprocessing import LabelBinarizer


def logloss(y_true, y_pred, eps=0.0001):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    lb = LabelBinarizer()
    labels = lb.fit(y_true).transform(y_true)
    preds = np.clip(y_pred, eps, 1-eps)
    if preds.ndim == 1:
        preds = preds[:, np.newaxis]
    if preds.shape[1] == 1:
        preds = np.append(1 - preds, preds, axis=1)
    if labels.shape[1] == 1:
        labels = np.append(1-labels, labels, axis=1)
    preds /= np.sum(preds, axis=1)[:, np.newaxis]
    return -np.sum(labels * np.log(preds))/preds.shape[0]


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(np.array(y_true) == np.array(y_pred))/len(y_true)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_y, pred_y = np.array(y_true), np.array(y_pred)
    if np.sum(pred_y) == 0:
        return 0.0
    else:
        return np.sum(true_y[pred_y == 1]) / np.sum(pred_y)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_y, pred_y = np.array(y_true), np.array(y_pred)
    if np.sum(true_y) == 0:
        return 0.0
    else:
        return np.sum(pred_y[true_y == 1]) / np.sum(true_y)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    true_y, pred_y = np.array(y_true), np.array(y_pred)
    by_pred = np.argsort(pred_y)
    true_y, pred_y = np.array([true_y[i] for i in by_pred]), np.array([pred_y[i] for i in by_pred])
    q = len(true_y)
    out = 0
    out_devis = 0
    for i in range(q):
        for j in range(q):
            devis = value_f(true_y[i], true_y[j])
            out += preds_f(pred_y[i], pred_y[j]) * devis
            out_devis += devis
    return out/out_devis if out_devis != 0 else 0


def preds_f(a1, a2):
    if a1 > a2:
        return 0
    elif a1 == a2:
        return 0.5
    else:
        return 1


def value_f(a1, a2):
    if a1 >= a2:
        return 0
    else:
        return 1
