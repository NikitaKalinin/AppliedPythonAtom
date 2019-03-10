#!/usr/bin/env python
# coding: utf-8


import pickle


with open('test_hw_02_vk_poster.ini.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
