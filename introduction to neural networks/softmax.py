#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:33:23 2019

This script defined the softmax algorithm.

The content of the file is provided by udacity through the 
Bertelsmann Tech challenge in AI Track

@author: moiseagbenya
"""

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    #compute exp for each value in the list
    expo_list = np.exp(L)
    return np.divide(expo_list, expo_list.sum())
