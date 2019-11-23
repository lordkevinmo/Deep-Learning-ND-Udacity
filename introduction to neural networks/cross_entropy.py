#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:34:52 2019

This script defined the cross entropy algorithm.

The content of the file is provided by udacity through the 
Bertelsmann Tech challenge in AI Track

@author: moiseagbenya
"""

import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    #We must convert first the values of Y and P to float
    #then we return the result of computation
    temp_y = np.float_(Y)
    temp_p = np.float_(P)
    return -np.sum(temp_y*np.log(temp_p) + (1-temp_y)*np.log(1-temp_p))