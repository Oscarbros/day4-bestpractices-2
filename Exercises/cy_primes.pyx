# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:16:11 2021

@author: oscbr226
"""

#Script to test out Cython. Recreating primes.py from the lecture slides.

def primes(int kmax):
    cdef int n, k, i 
    cdef int p[1000]
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