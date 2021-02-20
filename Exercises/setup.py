# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:40:32 2021

@author: oscbr226
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
      ext_modules = cythonize('cy_primes.pyx')
)