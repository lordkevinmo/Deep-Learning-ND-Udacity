#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:11:23 2019

@author: moiseagbenya
"""

import numpy as np

data = open('data/anna.txt', 'r').read()
chars = list(set(data))
print(chars)
s, l = len(data), len(chars)
print('data has %d characters, %d unique' % (s,l))
character_to_index = {ch:i for i,ch in enumerate(chars)}
index_to_character = {i:ch for i,ch in enumerate(chars)}

