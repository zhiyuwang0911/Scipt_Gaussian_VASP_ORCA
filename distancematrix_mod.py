import NPC
import numpy as np
import sys
import ase
import glob

#list and sort all .xyz file
full = glob.glob('*.xyz')
full.sort()

#create new .dat to store 'structure + distance value'
dis=open('distance_matrix.dat','w')
for i in full:
    q=NPC.quantumdot() #introduce function
    p=q.Readxyz(i)
    q.DistanceMatrix()  #introduce function
    M_center=q.atom.index('Fe')    #chose a element as operation center
    M_dismax=sum(q.dismatrix[M_center])  #sum through through bond from center to edge
    dis.write('{}    {:.10f}\n'.format(i[4:12], M_dismax))
dis.close()
