import NPC
import numpy as np
import sys

q=NPC.quantumdot()
q.Readxyz(sys.argv[1])

q.DistanceMatrix()
M_ind=q.atom.index('Fe')
M_dismax=sum(q.dismatrix[M_ind])

print(M_dismax)
