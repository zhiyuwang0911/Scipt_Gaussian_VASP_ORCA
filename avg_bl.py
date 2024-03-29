import ase
from ase import io
import os
import numpy as np
import glob
import re
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
bond = open('avg_bl.dat', 'w')
for i in file_list:
    xyz=io.read(i)
    cn = 4 #self-defined coordinate number
    #cn=int(i[5]) # coordinate number for single dopants
    reee=re.findall(r"\d+", i) 
    a3=reee[1:]
    #cn=np.sum([int(j) for j in a3])   #coordination number for mixture dopants
    an=list(xyz.arrays['numbers'])
    a1=list_duplicates_of(an, 26)
    a2=list(range(len(an)))
    a2.remove(a1[0])
    dist=xyz.get_distances(a1,a2)
    dist_sorted=np.sort(dist)
    avg_bl=np.mean(dist_sorted[:cn])
    bond.write('{}    {:.10f}\n'.format(i[:8], avg_bl))
bond.close()
