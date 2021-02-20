# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:55:11 2021

@author: oscbr226
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('The rank of the current process is: ' + str(rank))