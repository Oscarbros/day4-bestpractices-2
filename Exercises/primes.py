# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:34:50 2021

@author: oscbr226
"""

#Primes function from lecture notes 
import numpy as np

def primes(kmax):
    p = np.zeros((1000), dtype=np.int)
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0 
    n = 2 
    while k < kmax:
        i = 0 
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n 
            k = k + 1
            result.append(n)
        n = n + 1
    return result