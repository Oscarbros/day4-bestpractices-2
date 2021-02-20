# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:09:48 2021

@author: oscbr226
"""

#Script to calculate the sum over different parallel processes. 

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ranks = np.zeros(1)
total = np.zeros(1)
ranks[0] = np.sum(rank)

comm.Reduce(ranks, total, op=MPI.SUM, root=0)

if comm.rank == 0:
    print('Sum of all ranks ' + str(total))




# otherRank = rank

# if rank != 0:
#     otherRank = int(rank)
#     comm.Send(otherRank, dest=0)

# if rank == 0:
#     ranks = [rank]
#     for i in range(1,size):
#         sentRank = comm.Recv(otherRank, source=i)
#         ranks.append(int(sentRank))
#     sumRank = sum(ranks)
#     print('Sum of all ranks: ' + str(sumRank))