import ase
from ase import io
import os
import numpy as np
import glob
def list_duplicates_of(list1,elem):
    start_at = -1
    inds = []
    while True:
        try:
            ind = list1.index(elem,start_at+1)
        except ValueError:
            break
        else:
            inds.append(ind)
            start_at = ind
    return inds
file_list = glob.glob('*.xyz')
file_list.sort()
dis = open('metal_position.dat', 'w')
for i in file_list:
    xyz=io.read(i)
    an=list(xyz.arrays['numbers'])
    a1=list_duplicates_of(an, 26)  #Fe
    a2=list_duplicates_of(an, 1) # H
    dist=xyz.get_distances(a1,a2)
    distance=np.sum(dist)
    dis.write('{}    {:.10f}\n'.format(i[:8], distance))
dis.close()
