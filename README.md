# script
script
#get postion
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
dis = open('distance.dat', 'w')
for i in file_list:
    xyz=io.read(i)
    an=list(xyz.arrays['numbers'])
    a1=list_duplicates_of(an, 26)  #Fe
    a2=list_duplicates_of(an, 1) # H
    dist=xyz.get_distances(a1,a2)
    distance=np.sum(dist)
    dis.write('{}    {:.10f}\n'.format(i[:8], distance))
dis.close()


########################

#get averae bond length
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
bond = open('bond_len.dat', 'w')
for i in file_list:
    xyz=io.read(i)
    cn=int(i[5])
    an=list(xyz.arrays['numbers'])
    a1=list_duplicates_of(an, 26)
    a2=list(range(len(an)))
    a2.remove(a1[0])
    dist=xyz.get_distances(a1,a2)
    dist_sorted=np.sort(dist)
    avg_bl=np.mean(dist_sorted[:cn])
    bond.write('{}    {:.10f}\n'.format(i[:8], avg_bl))
bond.close()
-----------------------------------------------
